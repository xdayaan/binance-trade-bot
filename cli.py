import argparse
import sys
import json
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from dotenv import load_dotenv
from bot.client import BinanceBotClient
from bot.validators import validate_symbol, validate_side, validate_order_type, validate_quantity, validate_price
from bot.logging_config import setup_logging

# Load environment variables
load_dotenv()

logger = setup_logging()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    
    parser.add_argument('--symbol', type=str, required=True, help="Trading Pair (e.g., BTCUSDT)")
    parser.add_argument('--side', type=str, required=True, choices=['BUY', 'SELL'], help="Order Side (BUY/SELL)")
    parser.add_argument('--type', type=str, required=True, choices=['MARKET', 'LIMIT'], help="Order Type (MARKET/LIMIT)")
    parser.add_argument('--quantity', type=float, required=True, help="Order Quantity")
    parser.add_argument('--price', type=float, help="Order Price (Required for LIMIT orders)")

    args = parser.parse_args()

    try:
        # Validate inputs
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = None
        
        if order_type == 'LIMIT':
            if args.price is None:
                print("Error: --price is required for LIMIT orders.")
                sys.exit(1)
            price = validate_price(args.price)

        # Initialize Client
        client = BinanceBotClient()
        
        # Place Order
        response = client.place_order(symbol, side, order_type, quantity, price)
        
        # Print Output
        print("\n--- Order Summary ---")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if price:
            print(f"Price: {price}")
        
        print("\n--- Order Response ---")
        print(json.dumps(response, indent=2))
        print("\nSUCCESS: Order placed successfully.")

    except Exception as e:
        print(f"\nFAILURE: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
