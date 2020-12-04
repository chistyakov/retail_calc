import argparse
from argparse import Namespace
from decimal import Decimal

from calc.convert import str_to_decimal
from calc.tax import TAX_FACTOR_PER_STATE_CODE


def unmarshall_command_line_args() -> Namespace:
    parser = argparse.ArgumentParser(description="Retail calculator.")
    parser.add_argument(
        "--quantity", type=unmarshall_positive_int, help="Quantity of goods"
    )
    parser.add_argument(
        "--cost", type=unmarshall_not_negative_decimal, help="Cost of good (USD)"
    )
    parser.add_argument(
        "--state_code",
        type=str,
        help="State code",
        choices=list(TAX_FACTOR_PER_STATE_CODE),
    )
    parser.add_argument("--verbose", help="Verbose", default=False, action="store_true")
    args = parser.parse_args()
    return args


def unmarshall_positive_int(arg: str) -> int:
    try:
        value = int(arg)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{arg} is not valid int")

    if value <= 0:
        raise argparse.ArgumentTypeError(f"{arg} is not positive")

    return value


def unmarshall_not_negative_decimal(arg: str) -> Decimal:
    try:
        value = str_to_decimal(arg)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{arg} is not valid decimal")

    if value < 0:
        raise argparse.ArgumentTypeError(f"{arg} is not not negative")

    return value
