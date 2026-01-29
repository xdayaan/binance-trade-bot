# Binance Futures Trading Bot (Testnet)

A Python command-line application to place Market and Limit orders on the Binance Futures Testnet (USDT-M).

## Features
- Place **BUY** and **SELL** orders.
- Support for **MARKET** and **LIMIT** order types.
- Input validation for safe trading.
- clear logging of all API interactions.

## Setup

1. **Clone the repository** or extract the zip folder.

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys**
   Create a `.env` file in the `trading_bot` directory or set environment variables:
   ```bash
   export BINANCE_TESTNET_API_KEY='your_api_key'
   export BINANCE_TESTNET_API_SECRET='your_api_secret'
   ```
   *Note: Obtain these from the [Binance Testnet](https://testnet.binancefuture.com).*

## Usage

Run the bot from the `trading_bot` directory:

### Market Order
Buy 0.001 BTC at Market Price:
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order
Sell 0.001 BTC at $50,000:
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000
```

## Logs
Logs are saved to `trading_bot.log` and printed to the console.
