# Binance Futures Testnet Trading Bot

A Python-based command-line trading bot that places **Market** and **Limit** orders on the **Binance USDT-M Futures Testnet**. This project was developed as part of the PrimeTrade.ai Python Developer application task.

---

## Features

- Place **Market Orders**
- Place **Limit Orders**
- Supports both **BUY** and **SELL**
- Command-line interface using `argparse`
- Input validation
- Logging of API requests, responses, and errors
- Exception handling for API and network errors
- Environment variable support using `.env`

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── logs/
│   └── trading_bot.log
│
├── .env.example
├── .gitignore
├── cli.py
├── README.md
└── requirements.txt
```

---

## Requirements

- Python 3.10+
- Binance Futures Testnet Account
- Binance Testnet API Key & Secret

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/trading_bot.git
cd trading_bot
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_SECRET_KEY=YOUR_SECRET_KEY
```

---

## Usage

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 100000
```

---

## Example Output

### Market Order

```
========== SUCCESS ==========
Order ID      : 21611066395
Status        : FILLED
Executed Qty  : 0.0010
Average Price : 62648.500000
```

### Limit Order

```
========== SUCCESS ==========
Order ID      : 21615446160
Status        : NEW
Executed Qty  : 0.0000
Average Price : 0.00
```

---

## Logging

All API requests, responses, and errors are stored in:

```
logs/trading_bot.log
```

---

## Error Handling

The application handles:

- Invalid order type
- Invalid side
- Invalid quantity
- Missing price for limit orders
- Binance API exceptions
- Network-related exceptions
- Unexpected runtime errors

---

## Assumptions

- Uses Binance USDT-M Futures Testnet.
- Valid API credentials are configured in the `.env` file.
- Symbols used are supported by Binance Futures.

---

## Future Improvements

- Stop-Limit Orders
- Interactive CLI menu
- Position management
- Order cancellation
- Take Profit / Stop Loss support
- Web Dashboard using Streamlit or Flask

---

## Author

Lasya Sri Yarajarla