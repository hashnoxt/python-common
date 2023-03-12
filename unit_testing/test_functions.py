
from unittest import TestCase
from functions import divide

class TestFunctions(TestCase):
    def test_divide_result(self):
        dividend = 15
        divisor = 5
        expected_result = 5.0
        self.assertEqual(divide(dividend=dividend, divisor=divisor), expected_result)

