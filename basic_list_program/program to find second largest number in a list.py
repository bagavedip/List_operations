# program to find the second-largest number in the list
given_list = [1, 12, 13, 14]
maximum = given_list[0]
maximum_2 = given_list[1]
for i in given_list:
    if i > maximum:
        print("maximum number is" + str(i))

# program to find the second-largest number in the list using sorting method
test_list = [11, 18, 13, 17]
test_list.sort()
print(f"second largest element in list is {test_list[-2]}")

# program to find the second-largest number in the list using max method
test_list = [11, 12, 13, 10, 19, 18]
result = max(test_list)
given_list = test_list.remove(result)
maxi = max(test_list)
print(f"the second largest number is {maxi}")

# using list comprehension
def secondmax(arr):
    sublist = [x for x in arr if x < max(arr)]
    return max(sublist)


if __name__ == '__main__':
    arr = [10, 20, 4, 45, 99]
    print(secondmax(arr))

# find second-largest element in the list using sorted method
largest_list = [11, 12, 3, 2, 4 ,5]
largest = sorted(largest_list, reverse=True)
print(f" second largest element in list is {largest[1]}")
