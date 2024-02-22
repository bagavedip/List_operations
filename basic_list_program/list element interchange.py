# python program to interchange first and last element in list.
list = ["Dipika", "dhiraj", "renuka", "dheeraj"]
list[0], list[-1] = list[-1], list[0]
print[f"list is{list}"]


# python program to interchange first and last element in list.
def swaplist(list):
    start, *middle, end = list
    list = [end, *middle, start]
    return list


newlist = ["1", "2", "3", "4"]

print(swaplist(newlist))


# # python program to interchange first and last element in list.
def swaplist(list):
    """function for swaping program"""
    temp = list[0]
    list[0] = list[-1]
    list[-1] = temp
    return list


newlist = ["1", "2", "3", "4"]

print(swaplist(newlist))


# python program to interchange first and last element in list using slicing.
def swaplist(list):
    list = list[-1:] + list[1:-1] + list[:1]
    return list


newlist = ["Dhiraj", "renuka",]

print(swaplist(newlist))
