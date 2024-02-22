# Python3 code to demonstrate
# Sum of number digits in List
# using loop + str()

# Initializing list
test_list = [12, 67, 98, 34]
res_list = []
for digits in test_list:
    count = 0
    for i in str(digits):
        count += int(i)
    res_list.append(count)

print(f"the list of digit count is {res_list}")
