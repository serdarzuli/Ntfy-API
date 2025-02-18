import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NTFY_API_KEY")
BASE_URL = "https://ntfy.sh/"
