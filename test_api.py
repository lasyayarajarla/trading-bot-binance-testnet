from bot.client import client

try:
    print("Ping:", client.futures_ping())
    print("Server Time:", client.futures_time())
    print("Balance:", client.futures_account_balance())
except Exception as e:
    print("Error:", e)