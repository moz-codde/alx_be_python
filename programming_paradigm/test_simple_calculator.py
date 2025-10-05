import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(3, 2), 5)
        self.assertEqual(self.calc.add(1, -2), -1)
        self.assertEqual(self.calc.add(-2, -2), -4)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
        self.assertEqual(self.calc.subtract(4, -2), 6)
        self.assertEqual(self.calc.subtract(-1, 3), -4)
        self.assertEqual(self.calc.subtract(-2, -1), -1)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 2), 6)
        self.assertEqual(self.calc.multiply(7, 3), 21)
        self.assertEqual(self.calc.multiply(8, 0), 0)

    def test_division(self):
        self.assertEqual(self.calc.divide(8, 2), 4)
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsInstance(self.calc.divide(7, 2), float)

        