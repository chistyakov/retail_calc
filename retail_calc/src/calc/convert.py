from decimal import Decimal, DecimalException

TWOPLACES = Decimal(10) ** -2


def decimal_to_str(d: Decimal) -> str:
    try:
        return f"{d.quantize(TWOPLACES):.2f}"
    except DecimalException:
        raise ValueError


DENIED_DECIMAL = {Decimal("Infinity"), Decimal("-Infinity"), Decimal("Nan")}


def str_to_decimal(s: str) -> Decimal:
    try:
        d = Decimal(s)
    except DecimalException:
        raise ValueError

    if d in DENIED_DECIMAL:
        raise ValueError

    return d
