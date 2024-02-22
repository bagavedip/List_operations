# python program to find all positive numvers in range using for loop
test_list = []
for i in range(0, 12+1):
    if i >= 0:
        test_list.append(i)

print(test_list)

# python program to find out all positive element in between given range using list comprehensions
testt_list1 = [i for i in range(-20, 30) if i >= 0]
print(testt_list1)

# python program to find out positive numbers in list using enumerate method
a = -10
b = 30
result_list = []
for i in range(a, b+1):
    result_list.append(i)
test_list1 = [value for i, value in enumerate(result_list) if value >= 0]

# using pass method
tek_list = []
for i in range(-5, 10+1):
    if i < 0:
        pass
    else:
        tek_list.append(i)

print(tek_list)
