# Using the slicing technique
def cloning(test_list):
    test_list_copy = test_list[:]
    return test_list_copy


test_list = [11, 12, 13, 14]
test_list_copy = cloning(test_list)
print("after cloning test_list in test_list_copy is"+str(test_list_copy))
# Using the extend() method


def cloning(test_list_extend):
    copy_list = []
    copy_list.extend(test_list_extend)
    return copy_list


test_list_extend = [11, 13, 12, 14]
cpoy_list = cloning(test_list_extend)
print("copied list is" + str(cpoy_list))
# List copy using =(assignment operator)
test_list1 = [11, 12, 13, 14]
test_list_copy1 = test_list1
print("after coping list is" + str(test_list_copy1))
# Using the method of Shallow Copy
# importing copy method
import copy

# initializing list
test_list2 = [11, 12, 13, 14]
# making copy of test_list2 usig shallow copy method.
test_list_copy2 = copy.copy(test_list2)
# Using list comprehension

def cloning(test_list_3):
    clone = [i for i in test_list_3]
    return clone


test_list_3 = ["dhi", "dhiraj", "dipika"]
print("list is"+str(cloning(test_list_3)))
# Using the append() method

def coping(test_list_3):
    copy_list = []
    for i in test_list_3:
        copy_list.append(i)
    return copy_list


test_list_3 = ["dhi", "dhiraj", "dipika"]
print("copied ist is"+str(coping(test_list_3)))
# Using the copy() method
test_list_3 = ["dhi", "dhiraj", "dipika"]
copy_list = test_list_3.copy()
print("copied list using copy method is"+str(copy_list))
# Using the method of Deep Copy
test_copy = [11, 12, 13, 14, 15]
copied_list = copy.deepcopy(test_copy)
print("copied list using deepcopy is"+str(copied_list))
# Using the map method
lst = [4, 8, 2, 10, 15, 18]
copy_list = map(int, lst)
print(f"cpoed list using map function is{copy_list}")

# Using slice() function
lst = [4, 8, 2, 10, 15, 18]
li_copy = lst[slice(len(lst))]
print("Original List:", lst)
print("After Cloning:", li_copy)

# Using enumerate method
lst = [4, 8, 2, 10, 15, 18]
li_copy = [i for a, i in enumerate(lst)]
print("Original List:", lst)
print("After Cloning:", li_copy)
