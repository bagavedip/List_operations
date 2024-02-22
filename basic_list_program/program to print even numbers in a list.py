# program to find even number in the list using looping method
test_list = [11, 12, 13, 14, 16]
even_numbers = []
for i in test_list:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        continue

print(f"the even numbers in list are {even_numbers}")

# program to find even number in the list using while loop
test_list = [11, 12, 133, 22, 144]
num = 0
result_list = []
while num < len(test_list):
    if test_list[num] % 2 == 0:
        result_list.append(test_list[num])
    num += 1
print(f"the even numbers in list are {result_list}")

# using list comprehension
test_list = [1, 2, 3, 4, 6, 8]
test_result = [num for num in test_list if num % 2 == 0]
print(f" the even numbers in list are {test_result}")

