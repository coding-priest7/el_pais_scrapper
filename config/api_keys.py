from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

username = os.getenv("BROWSERSTACK_USERNAME", "default_username")
access_key = os.getenv("BROWSERSTACK_ACCESS_KEY", "default_access_key")
