from decimal import Decimal

from calc.discount import get_discount_factor


def total_price_without_tax(quantity: int, unit_cost: Decimal) -> Decimal:
    total = quantity * unit_cost
    discount_factor = get_discount_factor(total)
    return total * (Decimal("1.00") - discount_factor)
