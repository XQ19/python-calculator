import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    def test_add_1(self):
        self.assertEqual(self.calc.add(2, 2), 4)
    def test_add_2(self):
        self.assertEqual(self.calc.add(3, 2), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
    def test_subtract_1(self):
        self.assertEqual(self.calc.subtract(6, 2), 4)
    def test_subtract_2(self):
        self.assertEqual(self.calc.subtract(7, 2), 5)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
    def test_multiply_1(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
    def test_multiply_2(self):
        self.assertEqual(self.calc.multiply(9, 10), 90)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 2), 2)
    def test_divide_1(self):
        self.assertEqual(self.calc.divide(8, 4 ),2)
    def test_divide_1(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)
    def test_modulo_1(self):
        self.assertEqual(self.calc.modulo(7, 4), 3)
    def test_modulo_2(self):
        self.assertEqual(self.calc.modulo(8, 3), 2)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()