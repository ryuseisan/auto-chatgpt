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


class Chat:
    OPENAI_URL = "https://chat.openai.com/chat"

    def __init__(self, headless=True, wait=60):
        self.driver = self.set_driver(headless, wait)
        self.driver.get(Chat.OPENAI_URL)
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

    def get_driver(self):
        return self.driver

    def login(self):
        # login.bypassing_cloudflare(driver)
        login.click_login_button(self.driver)
        load_dotenv(verbose=True)
        EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
        PASSWORD = os.getenv("PASSWORD")
        login.login_openai(self.driver, email_address=EMAIL_ADDRESS, password=PASSWORD)
        login.skip_start_message(self.driver)

    def set_gpt_model(self, model):
        model_element_dic = {
            "GPT-3.5": "//span[contains(text(), 'Default (GPT-3.5)')]",
            "GPT-3.5-Legacy": "//span[contains(text(), 'Legacy (GPT-3.5)')]",
            "GPT-4": "//span[contains(text(), 'GPT-4')]",
        }
        self.driver.find_element(By.XPATH, '//div[@class="relative w-full md:w-1/2 lg:w-1/3 xl:w-1/4"]//button').click()
        self.driver.find_element(By.XPATH, model_element_dic.get(model)).click()

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
        self.driver.get(Chat.OPENAI_URL + f"/c/{chatid}")
