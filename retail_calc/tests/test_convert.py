import unittest
from decimal import Decimal

from calc.convert import str_to_decimal, decimal_to_str


class TestConvertStrToDecimal(unittest.TestCase):
    def test_convert_1(self):
        self.assertEqual(str_to_decimal("1"), Decimal("1.00"))

    def test_convert_123(self):
        self.assertEqual(str_to_decimal("1.23"), Decimal("1.23"))

    def test_convert_1234(self):
        self.assertEqual(str_to_decimal("1.234"), Decimal("1.234"))

    def test_convert_invalid_string(self):
        with self.assertRaises(ValueError):
            self.assertEqual(str_to_decimal("foobar"))

    def test_convert_infinity(self):
        with self.assertRaises(ValueError):
            self.assertEqual(str_to_decimal("Infinity"))


class TestConvertDecimalToStr(unittest.TestCase):
    def test_convert_1(self):
        self.assertEqual(decimal_to_str(Decimal("1")), "1.00")

    def test_convert_1234(self):
        self.assertEqual(decimal_to_str(Decimal("1.234")), "1.23")

    def test_convert_1236(self):
        self.assertEqual(decimal_to_str(Decimal("1.236")), "1.24")

    def test_convert_infinity(self):
        with self.assertRaises(ValueError):
            decimal_to_str(Decimal("Infinity"))
