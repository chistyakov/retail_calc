import unittest
from decimal import Decimal

from calc.total_price import total_price_without_tax


class TestPriceWithoutTax(unittest.TestCase):
    def test_quantity_1_cost_1(self):
        price = total_price_without_tax(quantity=1, unit_cost=Decimal("1.00"))
        self.assertEqual(price, Decimal("1.00"))

    def test_quantity_1000_cost_2(self):
        price = total_price_without_tax(quantity=1000, unit_cost=Decimal("2.00"))
        self.assertEqual(price, Decimal("1940.00"))
