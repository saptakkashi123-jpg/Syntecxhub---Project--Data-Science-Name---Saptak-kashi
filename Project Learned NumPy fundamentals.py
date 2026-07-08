# NumPy Fundamentals: Array Creation, Indexing, and Slicing

import numpy as np

# -------------------------------
# 1. Array Creation
# -------------------------------

# Creating a 1D array
arr1 = np.array([10, 20, 30, 40, 50])
print("1D Array:")
print(arr1)

# Creating a 2D array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
print("\n2D Array:")
print(arr2)

# Creating arrays using built-in NumPy functions
zeros = np.zeros((2, 3))
ones = np.ones((2, 2))
sequence = np.arange(1, 11)
even_numbers = np.arange(2, 21, 2)

print("\nZeros Array:")
print(zeros)

print("\nOnes Array:")
print(ones)

print("\nSequence Array:")
print(sequence)

print("\nEven Numbers:")
print(even_numbers)

# -------------------------------
# 2. Array Indexing
# -------------------------------

print("\nIndexing Examples:")

# Accessing elements in 1D array
print("First Element:", arr1[0])
print("Last Element:", arr1[-1])

# Accessing elements in 2D array
print("Element at Row 2, Column 3:", arr2[1, 2])
print("Element at Row 3, Column 1:", arr2[2, 0])

# -------------------------------
# 3. Array Slicing
# -------------------------------

print("\nSlicing Examples:")

# Slicing 1D array
print("First Three Elements:", arr1[:3])
print("Last Two Elements:", arr1[-2:])
print("Middle Elements:", arr1[1:4])

# Slicing 2D array
print("\nFirst Two Rows:")
print(arr2[:2])

print("\nFirst Two Columns:")
print(arr2[:, :2])

print("\nSubmatrix (Rows 1-2, Columns 2-3):")
print(arr2[0:2, 1:3])

# -------------------------------
# 4. Modifying Array Elements
# -------------------------------

arr1[2] = 100
print("\nModified 1D Array:")
print(arr1)

arr2[1, 1] = 50
print("\nModified 2D Array:")
print(arr2)
