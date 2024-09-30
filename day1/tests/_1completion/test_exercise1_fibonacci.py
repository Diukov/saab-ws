import unittest
from day1._1completion.exercise1_fibonacci import generate_fibonacci

class TestFibonacciSequenceGenerator(unittest.TestCase):
    def test_fibonacci_sequence(self):
        self.assertEqual(generate_fibonacci(0), [])
        self.assertEqual(generate_fibonacci(1), [0])
        self.assertEqual(generate_fibonacci(2), [0, 1])
        self.assertEqual(generate_fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(generate_fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

if __name__ == '__main__':
    unittest.main()
