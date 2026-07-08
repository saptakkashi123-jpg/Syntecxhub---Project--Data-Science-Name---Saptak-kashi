import numpy as np
import time

# -------------------------------
# Create Large Dataset
# -------------------------------

size = 1_000_000

python_list = list(range(size))
numpy_array = np.arange(size)

# -------------------------------
# Python List Performance
# -------------------------------

start = time.time()

python_result = [x * 2 for x in python_list]

end = time.time()

python_time = end - start

print("Python List Execution Time:")
print(f"{python_time:.6f} seconds")

# -------------------------------
# NumPy Array Performance
# -------------------------------

start = time.time()

numpy_result = numpy_array * 2

end = time.time()

numpy_time = end - start

print("\nNumPy Array Execution Time:")
print(f"{numpy_time:.6f} seconds")

# -------------------------------
# Performance Comparison
# -------------------------------

print("\nPerformance Comparison")

if numpy_time < python_time:
    speedup = python_time / numpy_time
    print(f"NumPy is approximately {speedup:.2f}x faster than Python lists.")
else:
    print("Python lists performed faster in this run (rare for large numerical operations).")

# -------------------------------
# Verify Results
# -------------------------------

print("\nFirst 10 Elements (Python List):")
print(python_result[:10])

print("\nFirst 10 Elements (NumPy Array):")
print(numpy_result[:10])
