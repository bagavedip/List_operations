# program to find duplicates in list using for loop.
def duplicates(test_list):
    element = []
    duplicate = []
    for i in test_list:
        if i not in element:
            element.append(i)
        elif i not in duplicate:
            duplicate.append(i)
    return duplicate


test_list = [1, 2, 3, 2, 1, 4, 5, 4]
print(f"{test_list} the duplicates are {duplicates(test_list)}")

# Using the Brute Force approach
def duplicate(list1):
    _size = len(list1)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if list1[i] == list1[j] and list1[i] not in repeated:
                repeated.append(list1[i])
    return repeated


list1 = [11, 12 ,13 ,122, 11]
print(duplicate(list1))
# Using Counter() function from collection module
from collections import Counter

test_list = [11, 12, 11, 12, 12]
result = Counter(test_list)
duplicate = list(item for item in result if result[item] > 1)
print(duplicate)
# Using count() method
given_list = [1, 2, 3, 2, 1, 3, 2]
duplicates = []
for i in given_list:
    num = given_list.count(i)
    if num > 1:
        if duplicates.count(i) == 0:
            duplicates.append(i)

print(f"duplicates are {duplicates}")

# Using list comprehension method
compre_list = [1, 2, 3, 2, 1, 3, 2]
result_list = list(set(i for i in compre_list if compre_list.count(i) > 1))
print(f"duplicates of list are {result_list}")
# Using list-dictionary approach (without any inbuild count function)
def duplicate(input_list):
    new_dict, new_list = {}, []

    for i in input_list:
        if not i in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1

    for key, values in new_dict.items():
        if values > 1:
            new_list.append(key)

    return new_list


if __name__ == '__main__':
    input_list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
    print(duplicate(input_list))

# Using in, not in operators and count() method


lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
x = []
y = []
for i in lis:
    if i not in x:
        x.append(i)
for i in x:
    if lis.count(i) > 1:
        y.append(i)
print(y)
# Using enumerate function
duple_list = [11, 12, 11, 111]
x = []
for i, value in enumerate(duple_list):
    if duple_list.count(value) > 1:
        x.append(value)

print(list(set(x)))
# Using operator.countOf() method
import operator as op
list2 = [11, 12, 13, 12, 14]
new_list = []
for i in list2:
    n = op.countOf(list2, i)
    if n > 1:
        if op.countOf(list2, i) > 1:
            new_list.append(i)
print(new_list)

 

