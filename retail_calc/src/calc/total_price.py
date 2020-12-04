from dataclasses import dataclass
from decimal import Decimal

from calc.discount import get_discount_factor
from calc.tax import get_tax_factor


@dataclass
class TotalPrice:
    # program should return 2 prices (see requirements)
    price: Decimal
    price_without_tax: Decimal


def total_price(quantity: int, unit_cost: Decimal, state_code: str) -> TotalPrice:
    without_tax = price_without_tax(quantity, unit_cost)
    tax_factor = get_tax_factor(state_code)
    price = without_tax * (Decimal("1.00") + tax_factor)
    return TotalPrice(price=price, price_without_tax=without_tax)


def price_without_tax(quantity: int, unit_cost: Decimal) -> Decimal:
    price = quantity * unit_cost
    discount_factor = get_discount_factor(price)
    return price * (Decimal("1.00") - discount_factor)
