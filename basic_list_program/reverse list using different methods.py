# Using the slicing technique
arr = ["dipika", "dhiraj", "dheeraj", "renuka"]
arr = arr[::-1]
print(arr)
# Reversing list by swapping present and last numbers at a time
# Using the reversed() and reverse() built-in function
arr = ["dipika", "dhiraj", "dheeraj", "renuka"]
print(list(reversed(arr)))
arr = ["dipika", "dhiraj", "dheeraj", "renuka"]
# reverse() method reverse list permanently.
arr.reverse()
print(arr)


# Using a two-pointer approach
def reverse_list(arr):
    left = 0
    right = len(arr) - 1
    while (left < right):
        # Swap
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
    return arr


arr = ["dipika", "dhiraj", "dheeraj", "renuka"]
reverse_list(arr)
# Using the insert() function
reverse_list = []
for i in arr:
    reverse_list.insert(0, i)
print(reverse_list)
# Using list comprehension
# Reversing a list using Numpy
import numpy as np

# Input list
my_list = [4, 5, 6, 7, 8, 9]

# Convert the list to a 1D numpy array
my_array = np.array(my_list)

# Reverse the order of the array
reversed_array = my_array[::-1]

# Convert the reversed array to a list
reversed_list = reversed_array.tolist()

# Print the reversed list
print(reversed_list)
