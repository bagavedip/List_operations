# python program to find all negative numbers in range using loop method
a = -10
b = 10
test_list = []
for i in range(a, b+1):
    if i < 0:
        test_list.append(i)

print(test_list)

# python program to find out negative numbers in range using list comprehensions
list1 = [i for i in range(-10, 10) if i < 0]
print(list1)

# python program to find out negative numbers in range using enumerate
list2 = [i for i in range(-10, 10)]
list_result = [i for v, i in enumerate(list2) if i < 0]

# using pass method
a = -4
b = 5
for i in range(a, b+1):
    if i >= 0:
        pass
    else:
        print(i, end=" ")
