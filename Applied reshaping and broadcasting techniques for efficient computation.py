import numpy as np

# -------------------------------
# Reshaping Arrays
# -------------------------------

# Create a 1D array
arr = np.arange(1, 13)
print("Original Array:")
print(arr)

# Reshape into 3 rows and 4 columns
reshaped = arr.reshape(3, 4)
print("\nReshaped Array (3x4):")
print(reshaped)

# Flatten back to 1D
flattened = reshaped.flatten()
print("\nFlattened Array:")
print(flattened)

# -------------------------------
# Broadcasting
# -------------------------------

# Add a scalar to every element
print("\nBroadcasting with Scalar (+10):")
print(reshaped + 10)

# Add a row vector to each row
row_vector = np.array([10, 20, 30, 40])
print("\nRow Vector:")
print(row_vector)

print("\nRow-wise Broadcasting:")
print(reshaped + row_vector)

# Add a column vector to each column
column_vector = np.array([[100], [200], [300]])
print("\nColumn Vector:")
print(column_vector)

print("\nColumn-wise Broadcasting:")
print(reshaped + column_vector)

# -------------------------------
# Element-wise Multiplication
# -------------------------------

multiplier = np.array([2, 2, 2, 2])

print("\nElement-wise Multiplication using Broadcasting:")
print(reshaped * multiplier)

# -------------------------------
# Mean Normalization using Broadcasting
# -------------------------------

mean = reshaped.mean(axis=0)
print("\nColumn Mean:")
print(mean)

normalized = reshaped - mean

print("\nMean Normalized Array:")
print(normalized)
