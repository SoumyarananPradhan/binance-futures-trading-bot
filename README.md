# Binance Futures Testnet Trading Bot

A Python-based command-line interface (CLI) application that places MARKET and LIMIT orders on the Binance Futures Testnet (USDT-M). Built with robust error handling, edge input validation, and comprehensive logging.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-repo-link>
   cd trading_bot

2. Create and activate a virtual environment:
python -m venv venv
# Windows
source venv/Scripts/activate
# Mac/Linux
source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Environment Variables:
Create a .env file in the root directory and add your Binance Testnet API credentials:

BINANCE_TESTNET_API_KEY=your_api_key_here
BINANCE_TESTNET_SECRET_KEY=your_secret_key_here

How to Run Examples
The application is executed via the command line using the argparse module.

Place a MARKET order (BUY):

python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.005

Place a LIMIT order (SELL):

python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.005 --price 95000

Assumptions & Architecture Environment: 

Assumes a valid .env file is present in the project root directory.

Testnet Exclusivity: 

The API client wrapper is strictly hardcoded to route to the Binance Futures Testnet (https://testnet.binancefuture.com).

Limit Order Expiration: 

Limit orders are hardcoded with a timeInForce of GTC (Good Till Canceled), as required by the Binance API for limit executions.

Architecture: 

The codebase follows a strictly modular architecture, cleanly separating the API client wrapper (client.py), core execution logic (orders.py), edge input validation (validators.py), system logging (logging_config.py), and the command-line interface (cli.py).

Author: Soumyaranjan Pradhan
