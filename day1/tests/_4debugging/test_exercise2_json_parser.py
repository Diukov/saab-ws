import unittest, os
from day1._4debugging.exercise2_json_parser import read_user_data

class TestJSONParser(unittest.TestCase):
    def setUp(self):
        self.valid_file = 'user_data_valid.json'
        self.invalid_file = 'user_data_invalid.json'
        with open(self.valid_file, 'w') as f:
            f.write('{"id": 1, "name": "Alice", "email": "alice@example.com"}')
        with open(self.invalid_file, 'w') as f:
            f.write('{"name": "Bob", "email": "bob@example.com"}')

    def test_valid_user_data(self):
        user_id, user_name, user_email = read_user_data(self.valid_file)
        self.assertEqual(user_id, 1)
        self.assertEqual(user_name, 'Alice')
        self.assertEqual(user_email, 'alice@example.com')

    def tearDown(self):
        if os.path.exists(self.valid_file):
            os.remove(self.valid_file)
        if os.path.exists(self.invalid_file):
            os.remove(self.invalid_file)

if __name__ == '__main__':
    unittest.main()
