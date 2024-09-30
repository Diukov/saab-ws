import unittest
from day1._3refactoring.exercise1_factorial import factorial

class TestFactorialFunction(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

if __name__ == '__main__':
    unittest.main()
