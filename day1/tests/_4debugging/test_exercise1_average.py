import unittest
from day1._4debugging.exercise1_average import calculate_average

class TestCalculateAverage(unittest.TestCase):
    def test_average_of_numbers(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3)
        self.assertEqual(calculate_average([10, 20, 30]), 20)

    def test_empty_list(self):
        result = calculate_average([])
        self.assertIsNone(result)

    def test_non_numeric_values(self):
        with self.assertRaises(TypeError):
            calculate_average(['a', 'b', 'c'])

if __name__ == '__main__':
    unittest.main()
