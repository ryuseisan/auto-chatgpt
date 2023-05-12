import os
import random
import time

import undetected_chromedriver as uc
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

from autochatgpt import login

# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait


class ChatGPTBot:
    OPENAI_URL = "https://chat.openai.com/chat"

    def __init__(self, headless=True, wait=60):
        self.driver = self.set_driver(headless, wait)
        self.driver.get(ChatGPTBot.OPENAI_URL)
        self.login()

    def set_driver(self, headless, wait_time):
        options = uc.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        driver = uc.Chrome(options=options)
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-dev-shm-usage')

        # wait for the page to load
        driver.implicitly_wait(wait_time)
        return driver

    def set_chat_history_and_training(self, check):
        # Open Data Controls settings window
        self.driver.find_element(By.XPATH, '//div[@class="group relative" and @data-headlessui-state=""]').click()
        self.driver.find_element(By.XPATH, '//a[contains(text(),"Settings")]').click()
        self.driver.find_element(By.XPATH, '//button[contains(., "Data controls")]').click()

        checked_value = self.driver.find_element(By.XPATH, "//button[@aria-checked]").get_attribute("aria-checked")
        if checked_value != check:
            # click Chat History and Training Button
            self.driver.find_element(By.XPATH, '//button[contains(@id, "headlessui-switch-")]').click()

        # close settings window
        self.driver.find_element(By.XPATH, '//div[@class="sm:mt-0"]/button').click()

    def get_driver(self):
        return self.driver

    def login(self):
        # login.bypassing_cloudflare(driver)
        login.click_login_button(self.driver)
        load_dotenv(verbose=True)
        EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
        PASSWORD = os.getenv("PASSWORD")
        ACCOUNT_TYPE = os.getenv("ACCOUNT_TYPE")
        if ACCOUNT_TYPE == "OPENAI":
            login.login_openai(self.driver, email_address=EMAIL_ADDRESS, password=PASSWORD)
        elif ACCOUNT_TYPE == "GOOGLE":
            login.login_google_account(self.driver, email_address=EMAIL_ADDRESS, password=PASSWORD)
        else:
            raise ValueError("ACCOUNT_TYPE must be OPENAI or GOOGLE")
        login.skip_start_message(self.driver)

    def set_gpt_model(self, model_version):
        if model_version not in ["GPT-3.5", "GPT-4"]:
            raise ValueError("model_version must be GPT-3.5 or GPT-4")
        self.driver.find_element(By.XPATH, f"//button[contains(., '{model_version}')]").click()

    def send_prompt(self, prompt):
        textarea = self.driver.find_element(By.CSS_SELECTOR, "textarea")
        textarea.clear()
        textarea.send_keys(prompt)
        time.sleep(random.uniform(1, 5))
        self.driver.find_element(By.CSS_SELECTOR, "button.absolute").click()

    def get_user_prompt(self):
        user_elements = self.driver.find_elements(
            By.XPATH,
            '//div[contains(@class, "group w-full text-gray-800 dark:text-gray-100 border-b border-black/10 dark:border-gray-900/50 dark:bg-gray-800")]',
        )
        return [user_element.text for user_element in user_elements]

    def get_gpt_response(self):
        gpt_elements = self.driver.find_elements(
            By.XPATH,
            '//div[contains(@class, "group w-full text-gray-800 dark:text-gray-100 border-b border-black/10 dark:border-gray-900/50 bg-gray-50 dark:bg-[#444654]")]',
        )
        return [gpt_element.text for gpt_element in gpt_elements]

    def resume_chat(self, chatid):
        self.driver.get(ChatGPTBot.OPENAI_URL + f"/c/{chatid}")
