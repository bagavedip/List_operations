# python program to remove empty list from list using for loop
test_list = [11, 12, 13, 12, [], []]
for i in test_list:
    if [] in test_list:
        test_list.remove([])

print(test_list)

# python program to remove empty list from list using for loop
test_list1 = [1, 1, 2, 3, [], []]
result = []
for i in test_list1:
    if i:
        result.append(i)

print(result)

# python program to remove empty list from list using list comprehension
list1 = [1, 2, 3, [], []]
result1 = [i for v, i in enumerate(list1) if i]
print(result1)

# Using filter() method
list_test = [1, 2, 3, 2, [], []]
result_test = [filter(None, list_test)]
print(result_test)

# Using the pop()
list_test = [1, 2, 3, 2, [], []]
i = 0
while i < len(list_test):
    if not list_test[i]:
        list_test.pop(i)
    else:
        i += 1
res = list_test
# Print the result
print("List after empty list removal : " + str(res))
