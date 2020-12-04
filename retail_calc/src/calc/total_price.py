from decimal import Decimal

from calc.discount import get_discount_factor
from calc.tax import get_tax_factor


def total_price(quantity: int, unit_cost: Decimal, state: str) -> Decimal:
    tax_factor = get_tax_factor(state)
    return total_price_without_tax(quantity, unit_cost) * (Decimal("1.00") + tax_factor)


def total_price_without_tax(quantity: int, unit_cost: Decimal) -> Decimal:
    total = quantity * unit_cost
    discount_factor = get_discount_factor(total)
    return total * (Decimal("1.00") - discount_factor)
