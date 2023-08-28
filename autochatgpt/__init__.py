import os

from dotenv import load_dotenv

load_dotenv(verbose=False)
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("PASSWORD")
ACCOUNT_TYPE = os.getenv("ACCOUNT_TYPE")
