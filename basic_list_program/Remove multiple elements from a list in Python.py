# remove multiple element from list using pop method
# (delete each element in the list which is divisible by 2 or all the even numbers.)


def multiple(test_list):
    for el, element in enumerate(test_list):
        try:
            if element % 2 == 0:
                test_list.remove(element)
            else:
                continue
        except Exception as e:
            print(e)
    return test_list


print(multiple(test_list=[11, 12, 13, 14, 18, 15, 16]))
# Python program to remove multiple
# elements from a list

# creating a list
list1 = [11, 5, 17, 18, 23, 50]

# removes elements from index 1 to 4
# i.e. 5, 17, 18, 23 will be deleted
del list1[1:5]

print(*list1)
