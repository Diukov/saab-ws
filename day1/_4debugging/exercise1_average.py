def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Example usage
if __name__ == "__main__":
    numbers = []
    average = calculate_average(numbers)
    print(f"The average is: {average}")

"""
Identify and fix the error in the function that calculates the average
of a list of numbers but raises an exception when the list is empty.
"""