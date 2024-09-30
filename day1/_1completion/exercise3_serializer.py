class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return f"User(name={self.name}, age={self.age}, email={self.email})"

def custom_serialize_user(user):
    """
    Manually serialize the User object into a JSON-like string.
    """
    # Use AI code completion here to manually construct the JSON-like string
    pass  # Remove this pass statement after completing the code

def custom_deserialize_user(serialized_data):
    """
    Manually deserialize the JSON-like string back into a User object.
    """
    # Use AI code completion here to manually parse the JSON-like string
    pass  # Remove this pass statement after completing the code

# Example usage
if __name__ == "__main__":
    # Create a User object
    user = User(name="Alice", age=30, email="alice@example.com")

    # Serialize the user object
    serialized_data = custom_serialize_user(user)
    print(f"Custom Serialized User: {serialized_data}")

    # Deserialize back to a User object
    deserialized_user = custom_deserialize_user(serialized_data)
    print(f"Custom Deserialized User: {deserialized_user}")
