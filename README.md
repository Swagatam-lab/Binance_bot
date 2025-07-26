# Binance Trading Bot 🤖📈

A simple Binance trading bot that interacts with the Binance API to fetch market data, execute trades, and manage account balances.

## 🚀 Features

- Fetches real-time cryptocurrency prices using Binance API.
- Allows buying and selling of selected crypto pairs.
- Calculates quantity based on current balance and market price.
- Automatically rounds the quantity according to Binance trading rules.

## 🛠️ Project Structure

Binance_bot/
│
├── api.py # Contains Binance API interaction logic
├── auth.py # Stores API key and secret securely
├── trade.py # Handles buy/sell trade logic
├── check_balance.py # Fetches and displays asset balances
└── main.py # Entry point for bot operations

markdown
Copy code

## 🔐 Requirements

- Python 3.7+
- Binance Account with API Key and Secret
- Installed Python packages from `requirements.txt`

## 📦 Installation

```bash
git clone https://github.com/Swagatam-lab/Binance_bot.git
cd Binance_bot
pip install -r requirements.txt
🔑 Setup
Create a auth.py file in the root directory with your Binance credentials:

python
Copy code
API_KEY = 'your_api_key_here'
API_SECRET = 'your_api_secret_here'
Important: Keep this file private and do not push it to GitHub.

⚙️ Usage
1. Check Balance
bash
Copy code
python check_balance.py
Displays your available balance in your Binance spot wallet.

2. Buy/Sell Crypto
Update trade.py with your preferred:

Trading symbol (e.g., BTCUSDT)

Order type (e.g., market)

Quantity logic

Then run:

bash
Copy code
python trade.py
3. Custom Trading Bot Logic
Write your strategy or logic in main.py to combine data fetching, balance checking, and trade execution.

bash
Copy code
python main.py
📘 Example
python
Copy code
from api import get_price
from trade import buy_crypto, sell_crypto

price = get_price("BTCUSDT")
print("Current BTC Price:", price)

buy_crypto("BTCUSDT", usdt_balance=50)
⚠️ Disclaimer
This bot is for educational purposes only. Use at your own risk. Cryptocurrency trading is highly volatile and you may lose your funds.

📄 License
MIT License

Made with 💻 by Swagatam
