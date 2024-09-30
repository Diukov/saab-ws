import unittest
from day1._1completion.exercise3_serializer import User, custom_serialize_user, custom_deserialize_user

class TestCustomSerializer(unittest.TestCase):
    def setUp(self):
        self.user = User(name="Alice", age=30, email="alice@example.com")
        self.serialized_data = '{"name": "Alice", "age": 30, "email": "alice@example.com"}'

    def test_custom_serialize_user(self):
        result = custom_serialize_user(self.user)
        self.assertEqual(result, self.serialized_data)

    def test_custom_deserialize_user(self):
        result = custom_deserialize_user(self.serialized_data)
        self.assertEqual(result.name, self.user.name)
        self.assertEqual(result.age, self.user.age)
        self.assertEqual(result.email, self.user.email)

if __name__ == "__main__":
    unittest.main()
