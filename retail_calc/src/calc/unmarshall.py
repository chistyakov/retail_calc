import argparse
from argparse import Namespace
from decimal import Decimal

from calc.convert import str_to_decimal
from calc.tax import TAX_FACTOR_PER_STATE


def unmarshall_command_line_args() -> Namespace:
    parser = argparse.ArgumentParser(description="Retail calculator.")
    parser.add_argument("--quantity", type=int, help="Quantity of units")
    parser.add_argument(
        "--unit_cost", type=unmarshall_decimal, help="Cost of unit (USD)"
    )
    parser.add_argument(
        "--state", type=str, help="State", choices=list(TAX_FACTOR_PER_STATE)
    )
    parser.add_argument("--verbose", type=bool, help="Verbose", default=False)
    args = parser.parse_args()
    return args


def unmarshall_decimal(arg: str) -> Decimal:
    try:
        return str_to_decimal(arg)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{arg} is not valid decimal")
