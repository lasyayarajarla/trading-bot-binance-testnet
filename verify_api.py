from pathlib import Path
import os
from dotenv import load_dotenv
from binance.client import Client

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

client = Client(
    os.getenv("BINANCE_API_KEY"),
    os.getenv("BINANCE_SECRET_KEY")
)

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

try:
    print(client.futures_account())
    print("✅ API works!")
except Exception as e:
    print("❌", e)