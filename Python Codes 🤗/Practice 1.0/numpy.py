import numpy as np

# From Python list
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# 2D Array (Matrix)
mat = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix:\n", mat)

# Special arrays
zeros = np.zeros((2, 3))   # 2x3 matrix of zeros
ones = np.ones((3, 3))     # 3x3 matrix of ones
rand = np.random.rand(2, 2) # Random values
arange = np.arange(1, 10, 2) # Values from 1 to 9 with step 2
