import unittest
import os
import json
from day1._2generation.exercise1_csv_to_json import csv_to_json

class TestCSVtoJSONConverter(unittest.TestCase):
    def setUp(self):
        self.csv_file = 'data/data.csv'
        self.json_file = 'data/data.json'
        if os.path.exists(self.json_file):
            os.remove(self.json_file)

    def test_conversion(self):
        csv_to_json(self.csv_file, self.json_file)
        self.assertTrue(os.path.exists(self.json_file))
        with open(self.json_file, 'r') as f:
            data = json.load(f)
        expected_data = [
            {"name": "Alice", "age": "30", "city": "New York"},
            {"name": "Bob", "age": "25", "city": "Los Angeles"},
            {"name": "Charlie", "age": "35", "city": "Chicago"}
        ]
        self.assertEqual(data, expected_data)

    def tearDown(self):
        if os.path.exists(self.json_file):
            os.remove(self.json_file)

if __name__ == '__main__':
    unittest.main()
