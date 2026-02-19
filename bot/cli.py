import argparse
import logging
from bot.logging_config import setup_logging
from bot.client import get_binance_client
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.orders import place_market_order, place_limit_order

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", "-s", required=True, help="Trading pair symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", "-d", required=True, help="Order side: BUY or SELL")
    parser.add_argument("--type", "-t", required=True, help="Order type: MARKET or LIMIT")
    parser.add_argument("--quantity", "-q", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", "-p", type=float, help="Price (Required for LIMIT orders)")

    args = parser.parse_args()

    setup_logging()
    logger = logging.getLogger(__name__)

    try:
        valid_symbol = validate_symbol(args.symbol)
        valid_side = validate_side(args.side)
        valid_type = validate_order_type(args.type)
        valid_qty = validate_quantity(args.quantity)
        valid_price = validate_price(valid_type, args.price)

        print("\n--- Order Request Summary ---")
        print(f"Symbol:     {valid_symbol}")
        print(f"Side:       {valid_side}")
        print(f"Type:       {valid_type}")
        print(f"Quantity:   {valid_qty}")
        if valid_type == 'LIMIT':
            print(f"Price:      {valid_price}")
        print("-----------------------------\n")

        print("Connecting to Binance Futures Testnet...")
        client = get_binance_client()

        response = None
        if valid_type == 'MARKET':
            response = place_market_order(client, valid_symbol, valid_side, valid_qty)
        elif valid_type == 'LIMIT':
            response = place_limit_order(client, valid_symbol, valid_side, valid_qty, valid_price)

        if response:
            print("\n--- Order Response Details ---")
            print(f"Status:       SUCCESS")
            print(f"Order ID:     {response.get('orderId')}")
            print(f"API Status:   {response.get('status')}")
            print(f"Executed Qty: {response.get('executedQty')}")
            
            avg_price = response.get('avgPrice')
            if avg_price and float(avg_price) > 0:
                print(f"Avg Price:    {avg_price}")
            print("------------------------------\n")

    except ValueError as ve:
        print(f"\n[Validation Error] {ve}")
        logger.warning(f"Validation failed: {ve}")
    except Exception as e:
        print(f"\n[Execution Failure] {e}")
        print("Please check the logs/trading_bot.log file for more details.")

if __name__ == "__main__":
    main()