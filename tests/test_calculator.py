import unittest
from app.calculator import add, multiply, subtract

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_subtract(self):
        self.assertEqual(subtract(9, 4), 5)

if __name__ == "__main__":
    unittest.main()
