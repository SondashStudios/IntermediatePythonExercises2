# Developer: Caius Iliesi
# Date: 1/30/2024

import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    start_time = time.time()

    # Generate a random number between 15 and 35 inclusive
    n = 34  # Replace with actual random number generation

    result = fibonacci(n)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"fib({n}) = {result}")
    print(f"fib({n}) took {elapsed_time} seconds")