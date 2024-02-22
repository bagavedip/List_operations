# clear list Using clear()
def list_clear(test_list):
    test_list.clear()
    return test_list


test_list = ["dipika", "dhiraj", "devalekar"]
list_clear(test_list)
print(test_list)
# Reinitializing the list
test_list1 = ["dhiraj", "dipika", "dheerakj"]
# Printing test_list1 before deleting
print("test_list1 before deleting is : "
      + str(test_list1))
test_list1 = []
# printing test_list1 after reinitialization
print("test_list1 after reinitialization is:" + str(test_list))
# Using “*= 0”
# Initializing lists
test = [11, 12, 12, 13]

# Printing list2 before deleting
print("test before clearing is : "
      + str(test))

test *= 0
# Printing list2 after reinitialization
print("test after clearing using *=0 : "
      + str(test))

# Using del
test_list2 = ["hello", "challo", "ohho"]
del test_list2[:]
print(f"after deleting list{test_list2}")
# Using pop() method
test_list3 = [11, 12, 13, 14]
while len(test_list3) != 0:
    test_list3.pop()
print("after poping out list is:"+str(test_list3))
# Using slicing
test_list4 = [11, 12, 13, 14]
lst = test_list4[:0]
print("test_list4 after deleting: is" + str(lst))
