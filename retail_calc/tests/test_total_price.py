import unittest
from decimal import Decimal

from calc.total_price import total_price, price_without_tax, TotalPrice


class TestTotalPrice(unittest.TestCase):
    def test_quantity_1_cost_1_state_UT(self):
        total = total_price(quantity=1, unit_cost=Decimal("1.00"), state='UT')
        self.assertEqual(total, TotalPrice(price=Decimal("1.0685"), price_without_tax=Decimal("1.00")))

    def test_quantity_5000_cost_2_state_AL(self):
        total = total_price(quantity=5000, unit_cost=Decimal("2.00"), state='AL')
        self.assertEqual(total, TotalPrice(price=Decimal("9360.00"), price_without_tax=Decimal("9000.00")))


class TestPriceWithoutTax(unittest.TestCase):
    def test_quantity_1_cost_1(self):
        price = price_without_tax(quantity=1, unit_cost=Decimal("1.00"))
        self.assertEqual(price, Decimal("1.00"))

    def test_quantity_1000_cost_2(self):
        price = price_without_tax(quantity=1000, unit_cost=Decimal("2.00"))
        self.assertEqual(price, Decimal("1940.00"))
