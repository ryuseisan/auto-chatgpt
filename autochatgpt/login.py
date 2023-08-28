"""This module contains functions for logging in to OpenAI's ChatGPT."""
import random
import time

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def click_login_button(driver: uc.Chrome) -> None:
    """Clicks the login button on the landing page.

    Args:
        driver (uc.Chrome): Selenium Chrome driver
    """
    driver.find_element(By.CSS_SELECTOR, 'button[data-testid="login-button"]').click()


def bypassing_cloudflare(driver: uc.Chrome) -> None:
    """Bypasses Cloudflare's anti-bot page.

    Args:
         driver (uc.Chrome): Selenium Chrome driver
    """
    # Wait for CloudFlare challenge-form to appear
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "challenge-form")))
    time.sleep(random.uniform(10, 15))
    driver.find_element(By.ID, "challenge-form").click()
    time.sleep(random.uniform(1, 5))


def login_openai(driver: uc.Chrome, email_address: str, password: str) -> None:
    """Login with your OpenAI account.

    Args:
        driver (uc.Chrome): Selenium Chrome driver
        email_address (str): Your OpenAI email address
        password (str): Your OpenAI password
    """
    # type email_address
    driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(email_address)

    time.sleep(random.uniform(1, 5))

    # click continue button
    driver.find_element(By.CSS_SELECTOR, 'button[name="action"]').click()

    # type user password
    driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(password)

    # click continue button
    continue_button = driver.find_element(By.CSS_SELECTOR, 'button[data-action-button-primary="true"]')
    time.sleep(random.uniform(1, 5))
    continue_button.click()


def login_google_account(driver: uc.Chrome, email_address: str, password: str) -> None:
    """Login with your Google account.

    Args:
        driver (uc.Chrome): Selenium Chrome driver
        email_address (str): Your Google email address
        password (str): Your Google password
    """
    # click the login button
    driver.find_element(By.CSS_SELECTOR, "button[data-provider='google']").click()
    time.sleep(random.uniform(1, 3))

    # type email address
    driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys(email_address)
    time.sleep(random.uniform(1, 3))

    # click next button
    driver.find_elements(By.TAG_NAME, "button")[3].click()
    time.sleep(random.uniform(1, 3))

    # type password
    try:
        driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(password)
    except Exception:
        driver.find_element(By.XPATH, '//input[@name="Passwd"]').send_keys(password)
    time.sleep(random.uniform(1, 3))

    # click next button
    driver.find_elements(By.TAG_NAME, "button")[1].click()


def skip_start_message(driver: uc.Chrome) -> None:
    """Skip the start message.

    Args:
        driver (uc.Chrome): Selenium Chrome driver
    """
    time.sleep(random.uniform(1, 3))
    driver.find_elements(By.CSS_SELECTOR, "button.btn-primary")[1].click()
