import numpy as np

# -------------------------------
# Create NumPy Arrays
# -------------------------------

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("Original Array 1:")
print(arr1)

print("\nOriginal Array 2:")
print(arr2)

# -------------------------------
# Save Single Array (.npy)
# -------------------------------

np.save("array1.npy", arr1)
print("\nSingle array saved as 'array1.npy'")

# -------------------------------
# Load Single Array
# -------------------------------

loaded_arr1 = np.load("array1.npy")

print("\nLoaded Array 1:")
print(loaded_arr1)

# -------------------------------
# Save Multiple Arrays (.npz)
# -------------------------------

np.savez("arrays.npz", first=arr1, second=arr2)
print("\nMultiple arrays saved as 'arrays.npz'")

# -------------------------------
# Load Multiple Arrays
# -------------------------------

loaded_arrays = np.load("arrays.npz")

print("\nLoaded First Array:")
print(loaded_arrays["first"])

print("\nLoaded Second Array:")
print(loaded_arrays["second"])

# -------------------------------
# Save Array as Text File (.txt)
# -------------------------------

np.savetxt("array2.txt", arr2, fmt="%d")
print("\nArray saved as 'array2.txt'")

# -------------------------------
# Load Array from Text File
# -------------------------------

loaded_txt = np.loadtxt("array2.txt", dtype=int)

print("\nLoaded Array from Text File:")
print(loaded_txt)
