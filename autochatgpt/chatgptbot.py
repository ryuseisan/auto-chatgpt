"""This module contains Class for automation in to OpenAI's ChatGPT."""
import random
import time

import undetected_chromedriver as uc
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from autochatgpt import AUTO_CHATGPT_ACCOUNT_TYPE, AUTO_CHATGPT_EMAIL_ADDRESS, AUTO_CHATGPT_PASSWORD, login

# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait


class ChatGPTBot:
    """ChatGPTBot."""

    OPENAI_URL = "https://chat.openai.com/"

    def __init__(self, headless: bool = True, wait: int = 60) -> None:
        """Initialize ChatGPTBot.

        Args:
            headless (bool, optional): headless. Defaults to True.
            wait (int, optional): implicitly_wait_time
        """
        self.implicitly_wait_time = wait
        self.driver = self.set_driver(headless, self.implicitly_wait_time)
        self.driver.get(ChatGPTBot.OPENAI_URL)

    def set_driver(self, headless: bool, wait_time: int) -> uc.Chrome:
        """Set driver.

        Args:
            headless (bool): headless
            wait_time (int): implicitly_wait_time
        """
        options = uc.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        driver = uc.Chrome(options=options)
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-dev-shm-usage')

        # wait for the page to load
        driver.implicitly_wait(wait_time)
        return driver

    def set_chat_history_and_training(self, check: bool) -> None:
        """Set Chat History and Training.

        Args:
            check (bool): True or False
        """
        # Open Data Controls settings window
        self.driver.find_element(By.XPATH, '//div[@class="group relative" and @data-headlessui-state=""]').click()
        self.driver.find_element(By.XPATH, '//a[contains(text(),"Settings")]').click()
        self.driver.find_element(By.XPATH, '//button[contains(., "Data controls")]').click()

        checked_value = self.driver.find_element(By.XPATH, "//button[@aria-checked]").get_attribute("aria-checked")
        checked_bool = True if checked_value == "true" else False

        if checked_bool != check:
            # click Chat History and Training Button
            self.driver.find_element(By.XPATH, '//button[contains(@role, "switch")]').click()

        # close settings window
        self.driver.find_element(By.XPATH, '//button[contains(@class, "inline-block")]').click()

    def get_driver(self) -> uc.Chrome:
        """Get driver.

        Returns
            uc.Chrome: driver
        """
        return self.driver

    def auto_login(
        self,
        email_address: str = AUTO_CHATGPT_EMAIL_ADDRESS,
        password: str = AUTO_CHATGPT_PASSWORD,
        account_type: str = AUTO_CHATGPT_ACCOUNT_TYPE,
    ) -> None:
        """Login to ChatGPT.

        Args:
            email_address (str, optional): Your email address.
                Defaults is AUTO_CHATGPT_EMAIL_ADDRESS environment variable.
            password (str, optional): Your password.
                Defaults is AUTO_CHATGPT_PASSWORD environment variable.
            account_type (str, optional): Your account type.
                Defaults is AUTO_CHATGPT_ACCOUNT_TYPE environment variable.

        Raises:
            ValueError: AUTO_CHATGPT_ACCOUNT_TYPE must be OPENAI or GOOGLE
        """
        # login.bypassing_cloudflare(driver)
        login.click_login_button(self.driver)

        if account_type == "OPENAI":
            login.login_openai(self.driver, email_address=email_address, password=password)
        elif account_type == "GOOGLE":
            login.login_google_account(self.driver, email_address=email_address, password=password)
        else:
            msg = "AUTO_CHATGPT_ACCOUNT_TYPE must be OPENAI or GOOGLE"
            raise ValueError(msg)
        login.skip_start_message(self.driver)

    def set_gpt_model(self, model_version: str) -> None:
        """Set GPT model.

        Args:
            model_version (str): GPT model version (GPT-3.5 or GPT-4)
        """
        if model_version not in ["GPT-3.5", "GPT-4"]:
            msg = "model_version must be GPT-3.5 or GPT-4"
            raise ValueError(msg)
        self.driver.find_element(By.XPATH, f"//button[contains(., '{model_version}')]").click()

    def send_prompt(self, prompt: str) -> None:
        """Send prompt.

        Args:
            prompt (str): Send prompt to ChatGPT
        """
        textarea = self.driver.find_element(By.CSS_SELECTOR, "textarea")
        textarea.clear()
        textarea.send_keys(prompt)
        time.sleep(random.uniform(1, 5))
        self.driver.find_element(By.CSS_SELECTOR, "button.absolute").click()

    # temporarily abolishing
    # def get_user_prompt(self):
    #     user_elements = self.driver.find_elements(
    #         By.XPATH,
    #         '//div[contains(@class, "group w-full text-gray-800 dark:text-gray-100 border-b border-black/10 dark:border-gray-900/50 dark:bg-gray-800")]',
    #     )
    #     return [user_element.text for user_element in user_elements]

    def get_gpt_response(self, timeout: int = 60) -> str:
        """Get GPT response.

        Args:
            timeout (int, optional): Timeout. Defaults to 60.
        """
        # Temporarily disable implicit wait
        self.driver.implicitly_wait(0)

        try:
            # Check if the element that is being output exists
            WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "result-streaming")]')),
            )

            # If it exists, wait until the output is finished
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located((By.XPATH, '//div[contains(@class, "result-streaming")]')),
            )
        except TimeoutException:
            # If the element doesn't exist, continue to get the text
            pass
        finally:
            # Re-enable implicit wait
            self.driver.implicitly_wait(self.implicitly_wait_time)

        # Get the element after the output is finished
        gpt_elements = self.driver.find_elements(
            By.XPATH,
            '//div[contains(@class, "markdown")]',
        )
        return [gpt_element.text for gpt_element in gpt_elements]

    def resume_conversation(self, chatid: str) -> None:
        """Resume conversation.

        Args:
            chatid (str): chatid
        """
        resume_chat_page = ChatGPTBot.OPENAI_URL + f"/c/{chatid}"
        self.driver.get(resume_chat_page)
        time.sleep(1)
        if self.driver.current_url != resume_chat_page:
            msg = "Unable to load conversation page. Check if the chatid is correct."
            raise ValueError(msg)
