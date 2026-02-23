import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/")

STANDARD_USER = os.getenv("STANDARD_USER", "standard_user")
LOCKED_USER = os.getenv("LOCKED_USER", "locked_out_user")
PASSWORD = os.getenv("PASSWORD", "secret_sauce")

HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
