import numpy as np

# Create a NumPy array of the first 10 positive integers
arr = np.arange(1, 11)

# Print the array
print("Original Array:", arr)

# Print the shape and data type
print("Shape:", arr.shape)
print("Data Type:", arr.dtype)

# Multiply each element by 2 and print the result
multiplied_arr = arr * 2
print("Array after multiplying by 2:", multiplied_arr)