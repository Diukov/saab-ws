import unittest
import os
from day1._3refactoring.exercise3_data_processor import DataProcessor  

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.input_file = 'data/input.csv'
        self.output_file = 'data/output.csv'
        with open(self.input_file, 'w') as f:
            f.write('apple,banana,carrot\n')
            f.write('dog,elephant,fox\n')
        self.processor = DataProcessor(self.input_file, self.output_file)

    def test_processing(self):
        self.processor.process()
        self.assertTrue(os.path.exists(self.output_file))
        with open(self.output_file, 'r') as f:
            lines = f.readlines()
        self.assertEqual(lines[0].strip(), 'APPLE,BANANA,CARROT')
        self.assertEqual(lines[1].strip(), 'DOG,ELEPHANT,FOX')

    def tearDown(self):
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

if __name__ == '__main__':
    unittest.main()
