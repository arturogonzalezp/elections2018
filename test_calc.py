import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 14)

    def test_substract(self):
        result = calc.substract(10, 5)
        self.assertEqual(result, 5)
    
    def test_multiply(self):
        result = calc.multiply(10,5)
        self.assertEqual(result, 50)
    
    def test_divide(self):
        result = calc.divide(10,5)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()

