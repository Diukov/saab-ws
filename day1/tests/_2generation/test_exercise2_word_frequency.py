import unittest
import os
from day1._2generation.exercise2_word_frequency import analyze_word_frequency

class TestWordFrequencyAnalyzer(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'frequency'
        os.makedirs(self.test_dir, exist_ok=True)
        with open(os.path.join(self.test_dir, 'file1.txt'), 'w') as f:
            f.write("Hello world\nHello")
        with open(os.path.join(self.test_dir, 'file2.txt'), 'w') as f:
            f.write("world of code\nCode world")

    def test_word_frequency(self):
        freq = analyze_word_frequency(self.test_dir)
        expected_freq = {
            'hello': 2,
            'world': 3,
            'of': 1,
            'code': 2
        }
        self.assertEqual(freq, expected_freq)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.test_dir)

if __name__ == '__main__':
    unittest.main()
