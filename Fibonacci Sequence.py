def fibonacci_sequence(n_terms):
    # Initialize the first two terms of the Fibonacci sequence
    fib_sequence = []
    
    # Generate the Fibonacci sequence
    for i in range(n_terms):
        if i == 0:
            fib_sequence.append(0)  # First term
        elif i == 1:
            fib_sequence.append(1)  # Second term
        else:
            # Next term is the sum of the previous two
            next_term = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_term)

    return fib_sequence

# Example usage:
try:
    num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
    if num_terms <= 0:
        print("Please enter a positive integer.")
    else:
        result = fibonacci_sequence(num_terms)
        print("Fibonacci sequence up to", num_terms, "terms:")
        print(result)
except ValueError:
    print("Please enter a valid integer.")
