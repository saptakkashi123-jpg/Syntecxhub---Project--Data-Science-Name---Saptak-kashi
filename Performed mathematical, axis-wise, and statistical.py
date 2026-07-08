import numpy as np

# -------------------------------
# Sample Dataset
# -------------------------------

data = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]])

print("Dataset:")
print(data)

# ===============================
# 1. Mathematical Operations
# ===============================

print("\n--- Mathematical Operations ---")

# Addition
print("Addition (+10):")
print(data + 10)

# Subtraction
print("\nSubtraction (-5):")
print(data - 5)

# Multiplication
print("\nMultiplication (*2):")
print(data * 2)

# Division
print("\nDivision (/10):")
print(data / 10)

# Square
print("\nSquare:")
print(np.square(data))

# Square Root
print("\nSquare Root:")
print(np.sqrt(data))

# Exponential
print("\nExponential:")
print(np.exp(data))

# ===============================
# 2. Axis-wise Operations
# ===============================

print("\n--- Axis-wise Operations ---")

# Sum
print("Column-wise Sum (axis=0):")
print(np.sum(data, axis=0))

print("\nRow-wise Sum (axis=1):")
print(np.sum(data, axis=1))

# Mean
print("\nColumn-wise Mean:")
print(np.mean(data, axis=0))

print("\nRow-wise Mean:")
print(np.mean(data, axis=1))

# Maximum
print("\nMaximum in each Column:")
print(np.max(data, axis=0))

print("\nMaximum in each Row:")
print(np.max(data, axis=1))

# Minimum
print("\nMinimum in each Column:")
print(np.min(data, axis=0))

print("\nMinimum in each Row:")
print(np.min(data, axis=1))

# ===============================
# 3. Statistical Operations
# ===============================

print("\n--- Statistical Operations ---")

print("Total Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))
print("Maximum Value:", np.max(data))
print("Minimum Value:", np.min(data))

# ===============================
# 4. Cumulative Operations
# ===============================

print("\n--- Cumulative Operations ---")

print("Cumulative Sum:")
print(np.cumsum(data))

print("\nCumulative Product:")
print(np.cumprod(data))

# ===============================
# 5. Logical Operations
# ===============================

print("\n--- Logical Operations ---")

print("Values Greater Than 50:")
print(data > 50)

print("\nElements Greater Than 50:")
print(data[data > 50])
