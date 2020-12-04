import unittest
from decimal import Decimal

from calc.calc import total_price_without_tax


class TestPriceWithoutTax(unittest.TestCase):
    def test_quantity_1(self):
        price = total_price_without_tax(quantity=1, unit_cost=Decimal("1"))
        self.assertEqual(price, Decimal("1"))
