"""
Sample user_data.json file:

{
    "name": "Alice",
    "email": "alice@example.com"
}
"""

import json

def read_user_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        user_id = data['id']
        user_name = data['name']
        user_email = data['email']
    return user_id, user_name, user_email

# Example usage
if __name__ == '__main__':
    user_data_file = 'data/user_data.json'
    user_id, user_name, user_email = read_user_data(user_data_file)
    print(f"User ID: {user_id}")
    print(f"Name: {user_name}")
    print(f"Email: {user_email}")

"""
Debug the program that reads data from a JSON file
but fails when the file does not contain the expected fields.
"""
