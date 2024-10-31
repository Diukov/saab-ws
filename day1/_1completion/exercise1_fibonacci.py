def generate_fibonacci(n):
    """
    Generates the Fibonacci sequence up to the n-th term.
    """
    sequence = []
    a = 0  # Initialize the first term
    b = 1  # Initialize the second term

    for _ in range(n):
        sequence.append(a)  # Add the current term to the sequence
        a, b = b, a + b  # Calculate the next term

    return sequence

# Example usage
if __name__ == "__main__":
    n_terms = 10
    fib_sequence = generate_fibonacci(n_terms)
    print(f"Fibonacci sequence up to {n_terms} terms: {fib_sequence}")
