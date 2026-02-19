import os
import logging
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException

logger = logging.getLogger(__name__)

def get_binance_client() -> Client:
    """
    Initializes and returns the Binance Futures Testnet client securely.
    """
    load_dotenv()
    
    api_key = os.getenv("BINANCE_TESTNET_API_KEY")
    api_secret = os.getenv("BINANCE_TESTNET_SECRET_KEY")

    if not api_key or not api_secret:
        error_msg = "API keys not found. Please ensure they are set in the .env file."
        logger.error(error_msg)
        raise ValueError(error_msg)

    try:
        client = Client(api_key, api_secret, testnet=True)
        
        client.futures_ping()
        logger.info("Successfully connected to the Binance Futures Testnet.")
        
        return client

    except BinanceAPIException as e:
        logger.error(f"Binance API Exception during connection: {e.status_code} - {e.message}")
        raise
    except Exception as e:
        logger.error(f"Unexpected network or system error connecting to Binance: {e}")
        raise