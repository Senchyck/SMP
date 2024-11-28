import unittest
import math
from calculator.operations import Calculator

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(Calculator.add(5, 3), 8)
        self.assertEqual(Calculator.add(-5, 3), -2)
        self.assertEqual(Calculator.add(0, 0), 0)
        self.assertEqual(Calculator.add(-5, -3), -8)

    def test_subtraction(self):
        self.assertEqual(Calculator.subtract(5, 3), 2)
        self.assertEqual(Calculator.subtract(-5, 3), -8)
        self.assertEqual(Calculator.subtract(0, 0), 0)
        self.assertEqual(Calculator.subtract(-5, -3), -2)

    def test_multiplication(self):
        self.assertEqual(Calculator.multiply(5, 3), 15)
        self.assertEqual(Calculator.multiply(-5, 3), -15)
        self.assertEqual(Calculator.multiply(5, 0), 0)
        self.assertEqual(Calculator.multiply(-5, -3), 15)

    def test_division(self):
        self.assertEqual(Calculator.divide(6, 3), 2)
        self.assertEqual(Calculator.divide(-6, 3), -2)
        self.assertEqual(Calculator.divide(-6, -3), 2)
        with self.assertRaises(ValueError):
            Calculator.divide(5, 0)

    def test_nan_and_infinity(self):
        # Test addition with NaN and infinity
        self.assertTrue(math.isnan(Calculator.add(math.nan, 1)))
        self.assertTrue(math.isnan(Calculator.add(1, math.nan)))
        self.assertTrue(math.isinf(Calculator.add(math.inf, 1)))
        self.assertTrue(math.isinf(Calculator.add(-math.inf, 1)))
        
        # Test subtraction with NaN and infinity
        self.assertTrue(math.isnan(Calculator.subtract(math.nan, 1)))
        self.assertTrue(math.isnan(Calculator.subtract(1, math.nan)))
        self.assertTrue(math.isinf(Calculator.subtract(math.inf, 1)))
        self.assertTrue(math.isinf(Calculator.subtract(-math.inf, 1)))

        # Test multiplication with NaN and infinity
        self.assertTrue(math.isnan(Calculator.multiply(math.nan, 1)))
        self.assertTrue(math.isnan(Calculator.multiply(1, math.nan)))
        self.assertTrue(math.isinf(Calculator.multiply(math.inf, 2)))
        self.assertTrue(math.isinf(Calculator.multiply(-math.inf, 2)))

        # Test division with NaN and infinity
        self.assertTrue(math.isnan(Calculator.divide(math.nan, 1)))
        self.assertTrue(math.isnan(Calculator.divide(1, math.nan)))
        self.assertTrue(math.isinf(Calculator.divide(math.inf, 1)))
        self.assertTrue(math.isinf(Calculator.divide(-math.inf, 1)))
        with self.assertRaises(ValueError):
            Calculator.divide(1, 0)

    def test_error_handling(self):
        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)

    def test_invalid_number(self):
        with self.assertRaises(ValueError):
            Calculator.add("a", 5)
        with self.assertRaises(ValueError):
            Calculator.subtract(5, "b")
        with self.assertRaises(ValueError):
            Calculator.multiply("x", "y")
        with self.assertRaises(ValueError):
            Calculator.divide(5, "z")
