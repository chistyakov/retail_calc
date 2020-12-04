#!/usr/bin/env python3

import argparse
import logging

from calc.convert import str_to_decimal, decimal_to_str
from calc.tax import TAX_FACTOR_PER_STATE
from calc.total_price import total_price

logger = logging.getLogger("retail_calc")


def main():
    parser = argparse.ArgumentParser(description="Retail calculator.")
    parser.add_argument("--quantity", type=int, help="Quantity of units")
    parser.add_argument("--unit_cost", type=_decimal, help="Cost of unit (USD)")
    parser.add_argument(
        "--state", type=str, help="State", choices=list(TAX_FACTOR_PER_STATE)
    )
    args = parser.parse_args()
    print(
        decimal_to_str(
            total_price(
                quantity=args.quantity,
                unit_cost=args.unit_cost,
                state=args.state,
            )
        )
    )


def _decimal(arg):
    try:
        return str_to_decimal(arg)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{arg} is not valid decimal")


if __name__ == "__main__":
    main()
