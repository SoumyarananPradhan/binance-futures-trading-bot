import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException

logger = logging.getLogger(__name__)

def place_market_order(client: Client, symbol: str, side: str, quantity: float) -> dict:
    """
    Places a MARKET order on Binance Futures.
    """
    try:
        logger.info(f"Request: Placing MARKET {side} order for {quantity} {symbol}")
        
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        
        logger.info(f"Response: MARKET order successful. Details: {response}")
        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error (MARKET): {e.status_code} - {e.message}")
        raise
    except BinanceOrderException as e:
        logger.error(f"Binance Order Error (MARKET): {e.status_code} - {e.message}")
        raise
    except Exception as e:
        logger.error(f"Unexpected network/system error (MARKET): {e}")
        raise

def place_limit_order(client: Client, symbol: str, side: str, quantity: float, price: float) -> dict:
    """
    Places a LIMIT order on Binance Futures.
    """
    try:
        logger.info(f"Request: Placing LIMIT {side} order for {quantity} {symbol} at price {price}")
        
        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='LIMIT',
            timeInForce='GTC',
            quantity=quantity,
            price=price
        )
        
        logger.info(f"Response: LIMIT order successful. Details: {response}")
        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error (LIMIT): {e.status_code} - {e.message}")
        raise
    except BinanceOrderException as e:
        logger.error(f"Binance Order Error (LIMIT): {e.status_code} - {e.message}")
        raise
    except Exception as e:
        logger.error(f"Unexpected network/system error (LIMIT): {e}")
        raise