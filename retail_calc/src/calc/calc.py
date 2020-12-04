from decimal import Decimal


def total_price_without_tax(quantity: int, unit_cost: Decimal) -> Decimal:
    total = quantity * unit_cost

    discount_factor = 0
    if total >= Decimal("1000"):
        discount_factor = Decimal("0.03")

    if total >= Decimal("5000"):
        discount_factor = Decimal("0.05")

    if total >= Decimal("7000"):
        discount_factor = Decimal("0.07")

    if total >= Decimal("10000"):
        discount_factor = Decimal("0.1")

    if total >= Decimal("50000"):
        discount_factor = Decimal("0.15")

    return total * (Decimal("1") - discount_factor)
