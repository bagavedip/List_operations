# program to find the smallest number in the list using min() method
import numpy as np

test_list = [10, 20, 30, 40, 100]
minimum = min(test_list)
print(f"minimum in list is:{minimum}")


# program to find the smallest number in the list using for loop
test_list = [10, 20, 30, 40, 100]
minimum = test_list[0]
number = 0
for i in test_list[1:]:
    if i < minimum:
        number = i
    else:
        number = minimum

print(f"minimum number in the list is:{number}")

# program to find the smallest number in the list using numpy array.
test_list = [10, 20, 30, 40, 100]
# first convert this list into array
test_array = np.array(test_list)
# find min using min method
minimum = test_array.min()
print(f"minimum number is:{minimum}")

# program to find the smallest number in the list using sort() method.
test_list = [10, 20, 30, 40, 100]
test_array.sort()
print(f"minimum number in list is {test_list[0]}")

# program to find the smallest number in the list using sort descending order.
test_list = [10, 20, 30, 40, 100]
test_list.sort(reverse=True)
print(f"minimum element in list is: {test_list[-1]}")

# Python code to print smallest element in the list
from functools import reduce
lst = [20, 10, 20, 15, 100]
print(reduce(min, lst))
