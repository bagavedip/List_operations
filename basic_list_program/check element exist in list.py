# using if statement check element present in list or not.
test_list = [1, 6, 3, 5, 3, 4]
element = 3
if element in test_list:
    print(f"{element} element present in list")
else:
    print("not exist")

# Using a loop
test_list = [1, 6, 3, 5, 3, 4]
for i in test_list:
    if i == 4:
        print("element is exist in list")
    else:
        continue

# Using any() function
test_list = [1, 6, 3, 5, 3, 4]
print(f"does any element contain in list:{any(test_list)}")
# Using count() function
test_list = [1, 6, 3, 5, 3, 4]
print(f"how many times element present in list {test_list.count(4)}")
# Using sort with bisect_left and set()
# Using find() method
test_list = [1, 6, 3, 5, 3, 4]
print("checking element present in list or not")
x = list(map(str, test_list))
y = "-".join(x)
if y.find("5", 0, 4) != -1:
    print("element present in list")
elif y.find("5", 0, -1) != -1:
    print("element present in list")
else:
    print("hello")
# Using Counter() function
from collections import Counter

test_list = [10, 15, 20, 7, 46, 2808]

# Calculating frequencies
frequency = Counter(test_list)

# If the element has frequency greater than 0
# then it exists else it doesn't exist

if frequency[15] > 0:
    print("Yes, 15 exists in list")
else:
    print("No, 15 does not exists in list")


# Using try-except block
def element_check(test_list):
    try:
        if 15 in test_list:
            return print("Element present in test_list")
    except Exception as error:
        return f"{error}"


test_list = [10, 15, 20, 7, 46, 2808]
element_check(test_list)
