import argparse
import sys

from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_type,
    validate_quantity,
    validate_price,
)


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading symbol (Example: BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        help="BUY or SELL"
    )

    parser.add_argument(
        "--type",
        required=True,
        help="MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Required only for LIMIT orders"
    )

    args = parser.parse_args()

    try:
        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_type(args.type)
        quantity = validate_quantity(args.quantity)

        price = None

        if order_type == "LIMIT":
            if args.price is None:
                raise ValueError("Price is required for LIMIT orders.")

            price = validate_price(args.price)

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {quantity}")

        if price:
            print(f"Price    : {price}")

        print("\nSending order...\n")

        response = place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
        )

        print("========== SUCCESS ==========")
        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Executed Qty  : {response.get('executedQty')}")
        avg_price = response.get("avgPrice") or response.get("price") or "N/A"

        print(f"Average Price : {avg_price}")

    except Exception as e:
        print("\n========== ERROR ==========")
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()