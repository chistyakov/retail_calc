import unittest
from decimal import Decimal

from parameterized import parameterized

from calc.tax import get_tax_factor


class TestTax(unittest.TestCase):
    @parameterized.expand(
        [
            ("UT", Decimal("0.0685")),
            ("NV", Decimal("0.08")),
            ("TX", Decimal("0.0625")),
            ("AL", Decimal("0.04")),
            ("CA", Decimal("0.0825")),
        ]
    )
    def test_tax_factor(self, input_state, expected_tax_factor):
        self.assertEqual(get_tax_factor(input_state), expected_tax_factor)

    def test_tax_factor_invalid(self):
        with self.assertRaises(ValueError):
            get_tax_factor('AA')
