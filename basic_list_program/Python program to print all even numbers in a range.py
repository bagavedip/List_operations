# program to print all even numbers in a range
def even_number(start, end):
    result = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            result.append(i)
        else:
            pass
    return result


print(f"the all even number between  4 and 15 are {even_number(4, 15)}")

# print all even numbers from list using range
for i in range(4, 15, 2):
    print(i, end="\t")

# using list comprehension
start = 6
end = 30
result = [i for i in range(start, end + 1, 2)]
print("\n" + str(result))

# using pass method


def even_num(start, end):
    result = []
    for i in range(start, end + 1):
        if i % 2 != 0:
            pass
        else:
            result.append(i)
    return result


print(f"even numbers are {even_num(6, 22)}")

# Python code To print all even numbers
# in a given range using numpy array
import numpy as np

# Declaring Range
a = 4
b = 15
li = np.array(range(a, b + 1))

# printing odd numbers using numpy array
even_num = li[li % 2 == 0]
print(even_num)
