import random
import time

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait


def set_driver(headless=False):
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)
    if headless:
        options.add_argument("--headless")
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')

    # wait for the page to load
    driver.implicitly_wait(60)
    return driver


def set_gpt_model(driver, model):
    model_element_dic = {
        "GPT-3.5": "//span[contains(text(), 'Default (GPT-3.5)')]",
        "GPT-3.5-Legacy": "//span[contains(text(), 'Legacy (GPT-3.5)')]",
        "GPT-4": "//span[contains(text(), 'GPT-4')]",
    }
    driver.find_element(By.XPATH, '//div[@class="relative w-full md:w-1/2 lg:w-1/3 xl:w-1/4"]//button').click()
    driver.find_element(By.XPATH, model_element_dic.get(model)).click()


def send_prompt(driver, prompt):
    textarea = driver.find_element(By.CSS_SELECTOR, "textarea")
    textarea.clear()
    textarea.send_keys(prompt)
    time.sleep(random.uniform(1, 5))
    driver.find_element(By.CSS_SELECTOR, "button.absolute").click()


def get_user_prompt(driver):
    user_elements = driver.find_elements(
        By.XPATH,
        '//div[contains(@class, "group w-full text-gray-800 dark:text-gray-100 border-b border-black/10 dark:border-gray-900/50 dark:bg-gray-800")]',
    )
    return [user_element.text for user_element in user_elements]


def get_gpt_response(driver):
    gpt_elements = driver.find_elements(
        By.XPATH,
        '//div[contains(@class, "group w-full text-gray-800 dark:text-gray-100 border-b border-black/10 dark:border-gray-900/50 bg-gray-50 dark:bg-[#444654]")]',
    )
    return [gpt_element.text for gpt_element in gpt_elements]
