# program to print positive numbers in list using loop
test_list = [11, 12, -1, -2, 11]
positive = []
for i in test_list:
    if i >= 0:
        positive.append(i)
print(positive)

# program to find positive numbers in list using list comprehensions
test_list = [11, 12, 13, 12, -1, -2]
list1 = [i for i in test_list if i >= 0]
print(list1)

# program to find positive numbers in list using enumerate
test_list = [11, 12 ,13, -1, -2]
list2 = [value for i, value in enumerate(test_list) if value >= 0]
print(list2)

# program to find positive numbers in list using while loop
list3 = [11, 12, 1, 2, -1, -2]
num = 0
posi = []
while num < len(list3):
    for i in list3:
        if i >= 0:
            posi.append(i)
        num += 1

print(posi)

