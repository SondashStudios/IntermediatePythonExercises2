# Developer: Caius Iliesi
# Date: 1/30/2024

import numpy as np

# Create a numpy list of 10 random floats between 0 and 1
random_floats = np.random.rand(10)

print("Random Numbers:")

# Print the random numbers
print(f"[{', '.join(map(str, random_floats))}]")

# Print mean, median, and standard deviation
print(f"Mean: {np.mean(random_floats)}, Median: {np.median(random_floats)}, Standard Deviation: {np.std(random_floats)}")

