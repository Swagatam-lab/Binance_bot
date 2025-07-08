import os
from dotenv import load_dotenv
from binance.client import Client
import logging
import sys

# Load API keys from .env
load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Initialize Binance Client
client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = 'https://fapi.binance.com/fapi'  # Futures endpoint

# Setup logging
logging.basicConfig(filename="bot.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def place_market_order(symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type="MARKET",
            quantity=quantity
        )
        logging.info(f"Market Order Placed: {order}")
        print("✅ Market Order placed successfully!")
    except Exception as e:
        logging.error(f"Market Order Failed: {e}")
        print("❌ Market Order failed:", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python market_orders.py <SYMBOL> <BUY/SELL> <QUANTITY>")
        sys.exit(1)

    symbol = sys.argv[1]
    side = sys.argv[2]
    quantity = float(sys.argv[3])
    place_market_order(symbol, side, quantity)
