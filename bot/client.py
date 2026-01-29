import os
from binance.client import Client
from binance.exceptions import BinanceAPIException
from .logging_config import setup_logging

logger = setup_logging()

class BinanceBotClient:
    def __init__(self):
        self.api_key = os.getenv('BINANCE_TESTNET_API_KEY')
        self.api_secret = os.getenv('BINANCE_TESTNET_API_SECRET')

        if not self.api_key or not self.api_secret:
            logger.error("API keys not found in environment variables.")
            raise EnvironmentError("Please set BINANCE_TESTNET_API_KEY and BINANCE_TESTNET_API_SECRET.")

        # Initialize Client for Testnet
        self.client = Client(self.api_key, self.api_secret, testnet=True)
        logger.info("Binance Client initialized on Testnet.")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        """
        Places an order on Binance Futures Testnet.
        """
        try:
            logger.info(f"Placing {side} {order_type} order for {quantity} {symbol}...")
            
            params = {
                'symbol': symbol,
                'side': side,
                'type': order_type,
                'quantity': quantity,
            }

            if order_type == 'LIMIT':
                if price is None:
                    raise ValueError("Price is required for LIMIT orders.")
                params['timeInForce'] = 'GTC'
                params['price'] = price

            response = self.client.futures_create_order(**params)
            
            logger.info(f"Order placed successfully: ID {response.get('orderId')}")
            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.message}")
            raise
        except Exception as e:
            logger.error(f"Unexpected Error: {str(e)}")
            raise
