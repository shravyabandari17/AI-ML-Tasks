# Task 1: NumPy Fundamentals
# Name: Bandari Shravya

import numpy as np

# 1. Creating NumPy Arrays
print("1. Creating NumPy Arrays")

arr1 = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr1)

arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("2D Array:")
print(arr2)


# 2. Array Indexing and Slicing
print("\n2. Array Indexing and Slicing")

print("First element of 1D array:", arr1[0])
print("Third element of 1D array:", arr1[2])

print("Elements from index 1 to 3:", arr1[1:4])

print("Element at row 1, column 2 of 2D array:", arr2[1, 2])
print("First row of 2D array:", arr2[0])
print("First two columns:")
print(arr2[:, 0:2])


# 3. Array Shape and Dimensions
print("\n3. Array Shape and Dimensions")

print("Shape of 1D array:", arr1.shape)
print("Dimensions of 1D array:", arr1.ndim)

print("Shape of 2D array:", arr2.shape)
print("Dimensions of 2D array:", arr2.ndim)


# 4. Basic Mathematical Operations
print("\n4. Basic Mathematical Operations")

numbers = np.array([10, 20, 30, 40, 50])

print("Array:", numbers)
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))
print("Sum:", np.sum(numbers))


# 5. Additional Mathematical Operations
print("\n5. Additional Mathematical Operations")

print("Addition:", numbers + 5)
print("Subtraction:", numbers - 5)
print("Multiplication:", numbers * 2)
print("Division:", numbers / 2)