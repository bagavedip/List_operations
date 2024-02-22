# python program to find out all negative numbers in list
list1 = [11, 12, 3, 4, -1, -2]
test_list = []
for i in list1:
    if i < 0:
        test_list.append(i)

print(test_list)

# python program to find all negative numbers using list comprehensions
list2 = [-1, -2, -3, -4, 11]
test_list1 = [i for i in list2 if i < 0]
print(test_list1)

# python program to find all negative numbers in list using enumerate method
list3 = [-1, -2, -3, -4, 11, 12]
test_list2 = []
for i, value in enumerate(list3):
    if value < 0:
        test_list2.append(value)

print(test_list2)

# python program to find all negative numbers in list using while loop
list4 = [-1, -2, -3, 11, 12]
num = 0
test_list = []
while num < len(list4):
    for i in list4:
        if i < 0:
            test_list.append(i)
        num += 1

print(test_list)


# Python program to print negative Numbers in a List
import numpy as np

# list of numbers
list1 = [-10, 21, 4, -45, -66, 93, -11]

# Using numpy to print the negative number
temp = np.array(list1)
neg_nos = temp[temp <= 0]

print("Negative numbers in the list: ", *neg_nos)
