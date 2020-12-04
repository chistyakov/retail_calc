import unittest
from decimal import Decimal

from parameterized import parameterized

from calc.discount import get_discount_factor


class TestDiscount(unittest.TestCase):
    @parameterized.expand(
        [
            (Decimal("999"), Decimal("0.00")),
            (Decimal("1000"), Decimal("0.03")),
            (Decimal("1001"), Decimal("0.03")),

            (Decimal("4999"), Decimal("0.03")),
            (Decimal("5000"), Decimal("0.05")),
            (Decimal("5001"), Decimal("0.05")),

            (Decimal("6999"), Decimal("0.05")),
            (Decimal("7000"), Decimal("0.07")),
            (Decimal("7001"), Decimal("0.07")),

            (Decimal("9999"), Decimal("0.07")),
            (Decimal("10000"), Decimal("0.10")),
            (Decimal("10001"), Decimal("0.10")),

            (Decimal("49999"), Decimal("0.10")),
            (Decimal("50000"), Decimal("0.15")),
            (Decimal("50001"), Decimal("0.15")),
            (Decimal("Infinity"), Decimal("0.15")),
        ]
    )
    def test_discount_factor(self, input_price, expected_discount_factor):
        self.assertEqual(get_discount_factor(input_price), expected_discount_factor)
