# program to multiply all numbers in lists using * operator in loop.
import numpy

number_list = [11, 1, 1, 2, 3, 14]
multiplication = 1
for i in number_list:
    multiplication *= i
print(f"multiplication of all numbers is {multiplication}")

# Using Traversal
# Using numpy.prod()
import numpy


number_list = [1, 2, 3, 4, 5, 22]
result = numpy.prod(number_list)
print(f"the multiplication of numbers is {result}")

# Using Math Library
import math


given_list = [1, 2, 1, 3, 11]
result = math.prod(given_list)
print(f"multiplication is {result}")
# Using mul() function

from operator import *

number_list = [11, 12, 11, 22, 11, 1]
m = 1
for i in number_list:
    m = mul(i, m)
print(f"multiplication is {m}")
# Using traversal by index
def multiply(mylist):
    number = 1
    for i in range(0, len(mylist)):
        number = number * mylist[i]
    return number

mylist = [1, 2, 1, 2, 3, 4]
print(f"the multiplication is {multiply(mylist)}")

# Using reduce and mul function


from functools import reduce
from operator import mul

list1 = [1, 2, 3]
result = reduce(mul, list1)

print(result)