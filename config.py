import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Key & URL
API_URL = os.getenv("API_URL")  # Ensure this key exists in .env
CURRENCY_LIST = ["bitcoin", "ethereum", "xrp", "tether", "bnb"]  # Define currencies
TOP_N = 5  # Number of top cryptocurrencies to display
