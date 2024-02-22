# python program to count positive and negative numbers in list
list1 = [10, 12, 12, 13, -1, -2, -3]
positive = []
negative = []
for i in list1:
    if i < 0:
        negative.append(i)
    elif i >= 0:
        positive.append(i)

print(f"the count of negative numbers is {len(negative)} and postive count is {len(positive)}")

# python program to count positive and negative numbers in list using while loop
list2 = [11, 12, 13, -1, -2, -20, -40]
num = 0
pos = 0
neg = 0
while num < len(list2):
    if list2[num] < 0:
        neg += 1
    elif list2[num] >= 0:
        pos += 1
    num += 1

print(f"negative count is {neg} and positive count is {pos}")

# python program to count positive and negative numbers in list using list comprehensions

# list of numbers
list1 = [-10, -21, -4, -45, -66, -93, 11]

only_pos = [num for num in list1 if num >= 1]
pos_count = len(only_pos)

print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", len(list1) - pos_count)

# python program to count positive and negative numbers in list using enumerate


l = [12, -7, 5, 64, -14]
c = 0
x = [a for j, a in enumerate(l) if a >= 0]
print("Length of Positive numbers is:", len(x))
print("Length of Negative numbers is:", len(l)-len(x))

# using sum method
l = [12, -7, 5, 64, -14]
x = sum(1 for i in l if i >= 0)
print("Length of Positive numbers is:", x)
print("Length of Negative numbers is:", len(l)-x)
