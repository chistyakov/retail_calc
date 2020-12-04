from decimal import Decimal


def total_price_without_tax(quantity: int, unit_cost: Decimal) -> Decimal:
    return quantity * unit_cost
