# program to find the largest number in list with max() method
test_list = [1, 2, 3, 4, 5]
print(max(test_list))

# using loop on list
test_list = [2, 1, 3, 4, 5]
maximum = test_list[0]
for i in test_list[1:]:
    if i > maximum:
        max = i
test_list.remove(maximum)
print(f"max is:{max}")

# find the largest number in the list using sort() method


def largest(test_list):
    test_list.sort()
    return test_list[-1]



test_list = [11, 20, 13]
print(largest(test_list))

# python code to print largest element in the list

# lst = [20, 10, 20, 4, 100]
# print(max(lst, key=lambda value: int(value)))


# find the largest number using numpy array method
import numpy as np

test_list = [20, 30, 10, 60]
# first convert thos list to array
array_list = np.array(test_list)
# then find max using max method
maximum = array_list.max()
print(f"maximum nomber is:{maximum}")
