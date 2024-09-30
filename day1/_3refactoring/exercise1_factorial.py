def factorial(n):
    """
    Calculates the factorial of n using recursion.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
if __name__ == "__main__":
    number = 5
    print(f"The factorial of {number} is: {factorial(number)}")

"""
Refactor the recursive factorial function to use iteration instead,
improving efficiency and avoiding maximum recursion depth issues.
"""