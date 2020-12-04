import unittest
from decimal import Decimal

from calc.calc import total_price_without_tax


class TestPriceWithoutTax(unittest.TestCase):
    def test_quantity_1(self):
        price = total_price_without_tax(quantity=1, unit_cost=Decimal("1.00"))
        self.assertEqual(price, Decimal("1.00"))

    def test_quantity_2(self):
        price = total_price_without_tax(quantity=2, unit_cost=Decimal("1.00"))
        self.assertEqual(price, Decimal("2.00"))

    def test_quantity_999(self):
        price = total_price_without_tax(quantity=999, unit_cost=Decimal("1.00"))
        self.assertEqual(price, Decimal("999.00"))

    def test_quantity_1000(self):
        price = total_price_without_tax(quantity=1000, unit_cost=Decimal("1.00"))
        self.assertEqual(price, Decimal("970.00"))

    def test_quantity_4999(self):
        price = total_price_without_tax(quantity=4999, unit_cost=Decimal("1.00"))
        self.assertEqual(price, Decimal("4849.03"))

    def test_quantity_5000(self):
        price = total_price_without_tax(quantity=5000, unit_cost=Decimal("1.00"))
        self.assertEqual(price, Decimal("4750.00"))

    def test_quantity_49999(self):
        price = total_price_without_tax(quantity=49999, unit_cost=Decimal("1.00"))
        self.assertEqual(price, Decimal("44999.10"))

    def test_quantity_50000(self):
        price = total_price_without_tax(quantity=50000, unit_cost=Decimal("1.00"))
        self.assertEqual(price, Decimal("42500.00"))
