from bisect import bisect
from decimal import Decimal

DISCOUNT_BREAKPOINTS = (
    Decimal("1000"),
    Decimal("5000"),
    Decimal("7000"),
    Decimal("10000"),
    Decimal("50000"),
)
DISCOUNT_FACTORS = (
    Decimal("0.00"),
    Decimal("0.03"),
    Decimal("0.05"),
    Decimal("0.07"),
    Decimal("0.10"),
    Decimal("0.15"),
)


def get_discount_factor(price: Decimal) -> Decimal:
    i = bisect(DISCOUNT_BREAKPOINTS, price)
    return DISCOUNT_FACTORS[i]
