import numpy as np

# 1. Create an array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# 2. Difference between list and array
py_list = [1, 2, 3, 4, 5]
print("Python List * 2:", py_list * 2)   # repeats list
print("NumPy Array * 2:", arr * 2)       # multiplies each element

# 3. Basic operations
print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Max:", arr.max())

# 4. Multi-dimensional array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix:\n", matrix)
print("Shape:", matrix.shape)

# 5. Slicing
print("First row:", matrix[0])
print("Second column:", matrix[:, 1])

# 6. Reshape
reshaped = np.arange(1, 10).reshape(3, 3)
print("Reshaped 3x3:\n", reshaped)
