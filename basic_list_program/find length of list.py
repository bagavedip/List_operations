# Find length of list Using len() function
list = ["dipika", "dhiraj", "dheeraj", "renuka"]
print(len(list))
# Using Naive Method
list = ["dipika", "dhiraj", "dheeraj", "renuka"]
counter = 0
for i in list:
    counter += 1
print(f"Length of the list is {counter}")

# Using length_hint()
from operator import length_hint


list = ["dipika", "dhiraj", "dheeraj", "renuka"]
print(length_hint(list))
# Using sum() method
list = ["dipika", "dhiraj", "dheeraj", "renuka"]
length = sum(1 for s in list)
print(f"length in list is {length}")
# Using a list comprehension
list = ["dipika", "dhiraj", "dheeraj", "renuka"]
print(sum(1 for i in list))
# Using enumerate function
counter = 0
for i, value in enumerate(list):
    counter +=1
print(f"length of list is {counter}")
# Using Collections Module
from collections import Counter
list = ["dipika", "dhiraj", "dheeraj", "renuka"]
len_list = sum(Counter(list).values())
print(len_list)