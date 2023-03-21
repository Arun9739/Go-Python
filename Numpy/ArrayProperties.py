
# This program prints the properties of numpy array such as size, shape etc.

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Printing properties
print("Type of array : ", type(arr))

print("Elements of the array are of type : ", arr.dtype)

print("Shape of the array : ", arr.shape)

print("No. of dimensions : ", arr.ndim)

print("Size of the array : ", arr.size)


