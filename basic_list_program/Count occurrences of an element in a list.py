# Using a loop in Python
count_list_1 = [10, 12, 11, 10, 11, 12, 11, 13, 12, 12]
count_list = []
for i in count_list_1:
    if i == 12:
        count_list.append(i)
    else:
        continue
print(f"list of 12 element count is{len(count_list)}")
# Using List Comprehension
count_list_1 = [10, 12, 11, 10, 11, 12, 13, 13, 13, 13]
count_list = [i for i in count_list_1 if i == 12]
print(f"list in count of 12 is {len(count_list)}")
# Using enumerate function
count_of_list = []
for i, value in enumerate(count_list_1):
    if i == 13:
        count_of_list.append(i)
    else:
        continue
print(f"value of 13 element present in list is {len(count_of_list)}")
# Using count()
count_list = [10, 12, 11, 10, 11, 12, 11, 13]
counting = count_list.count(11)
print(f"counting of 11 in list is {counting}")

# Using Counter()
from collections import Counter


count_list = [10, 12, 11, 10, 11, 12, 11, 13]
count_list_of = Counter(count_list)
print(f"counting of element in list is{count_list_of[12]}")
# Using countOf()


import operator as op

# declaring list
test_list = [11, 12, 13, 12, 12, 13, 13, 11]
count_list = op.countOf(test_list, 12)
print(f"count of emement 12 in list is {count_list}")
# Using dictionary comprehension


lis = ['a', 'd', 'd', 'c', 'a', 'b', 'b', 'a', 'c', 'd', 'e']
occurrence = {item: lis.count(item) for item in lis}
print(occurrence.get('e'))
# Using Pandas’s Library
import pandas as pd

# declaring the list
l = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]

count = pd.Series(l).value_counts()
print("Element Count")
print(count)
