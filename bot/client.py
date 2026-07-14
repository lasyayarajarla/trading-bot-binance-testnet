from pathlib import Path
import os
from dotenv import load_dotenv
from binance.client import Client

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_SECRET_KEY")

if not API_KEY or not API_SECRET:
    raise ValueError("API credentials not found.")

client = Client(
    api_key=API_KEY,
    api_secret=API_SECRET,
    testnet=True
)

def get_client():
    return client