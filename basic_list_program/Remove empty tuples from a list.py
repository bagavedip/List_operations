# remove empty tuple from the list using loop
test_list = [0, 1, 2, (1, 2), (), (), ()]
for i in test_list:
    if () in test_list:
        test_list.remove(())
    else:
        continue

print(test_list)

# remove empty tuple from list using list comprehensions


def remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples


test_lis = [11, 12, 13, 14, 12, (), ()]
print(remove(test_lis))

# python program to remove empty tuples from list


def removes(tuples):
    tuples = filter(None, tuples)
    return tuples


given_list = [11, 12, 13, (), ()]
print(removes(given_list))


# remove empty tuples from list using len() methods
test_lists = [12, (), ('ram', '15', '8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('', ''), (), 11]
try:
    for i in test_lists:
        if type(i) is not int:
            if len(i) == 0:
                test_lists.remove(i)
            else:
                continue
    print(test_lists)
except Exception as e:
    print(e)

# remove empty tuple from the list using == operator


def removs(test_list):
    for test in test_list:
        if test == ():
            test_list.remove(test)
    return test_list


test_list = [0, 1, 2, (1, 2), (), 11, ()]
print(removs(test_list))

