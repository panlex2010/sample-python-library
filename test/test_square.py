import sys
import unittest

print(f"sys.path: {sys.path}")
from src.square import Square

class SquareTest(unittest.TestCase):
    def setUp(self):
        self.square = Square(5)

    def test_perimeter_positive(self):
        self.assertEqual(self.square.perimeter(), 20)

    def test_perimeter_negative(self):
        self.assertNotEqual(self.square.perimeter(), 10)

    def test_area_positive(self):
        self.assertEqual(self.square.area(), 25)

    def test_area_negative(self):
        self.assertNotEqual(self.square.area(), 10)

if __name__ == '__main__':
    unittest.main()
