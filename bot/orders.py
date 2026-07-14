from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException

from bot.client import get_client
from bot.logging_config import logger

client = get_client()


def place_order(symbol, side, order_type, quantity, price=None):
    """
    Places a Futures order on Binance Testnet.

    Parameters:
        symbol (str)
        side (BUY / SELL)
        order_type (MARKET / LIMIT)
        quantity (float)
        price (float | None)

    Returns:
        API response dictionary
    """

    try:
        logger.info("========== ORDER REQUEST ==========")
        logger.info(
            f"Symbol={symbol}, Side={side}, Type={order_type}, "
            f"Quantity={quantity}, Price={price}"
        )

        if order_type == "MARKET":

            # Place Market Order
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=FUTURE_ORDER_TYPE_MARKET,
                quantity=quantity
            )

            # Fetch latest order details
            response = client.futures_get_order(
                symbol=symbol,
                orderId=response["orderId"]
            )

        elif order_type == "LIMIT":

            # Place Limit Order
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=FUTURE_ORDER_TYPE_LIMIT,
                quantity=quantity,
                price=price,
                timeInForce=TIME_IN_FORCE_GTC
            )

            # Fetch latest order details
            response = client.futures_get_order(
                symbol=symbol,
                orderId=response["orderId"]
            )

        else:
            raise ValueError("Unsupported order type.")

        logger.info("========== ORDER RESPONSE ==========")
        logger.info(response)

        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise

    except BinanceOrderException as e:
        logger.error(f"Order Error: {e}")
        raise

    except Exception as e:
        logger.exception(f"Unexpected Error: {e}")
        raise