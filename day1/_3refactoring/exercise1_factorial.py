def factorial(n):
    """
    Calculates the factorial of n using iteration.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
if __name__ == "__main__":
    number = 5
    print(f"The factorial of {number} is: {factorial(number)}")

"""
Refactor the recursive factorial function to use iteration instead,
improving efficiency and avoiding maximum recursion depth issues.
"""