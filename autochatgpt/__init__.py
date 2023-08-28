import os

from dotenv import load_dotenv

load_dotenv(verbose=False)
AUTO_CHATGPT_EMAIL_ADDRESS = os.getenv("AUTO_CHATGPT_EMAIL_ADDRESS")
AUTO_CHATGPT_PASSWORD = os.getenv("AUTO_CHATGPT_PASSWORD")
AUTO_CHATGPT_ACCOUNT_TYPE = os.getenv("AUTO_CHATGPT_ACCOUNT_TYPE")
