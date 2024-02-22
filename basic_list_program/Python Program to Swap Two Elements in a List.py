# Python Program to Swap Two Elements in a List
newlist = ["12", "13", "14", "15"]
pos1 = 1
pos2 = 3
newlist[pos1-1], newlist[pos2-1] = newlist[pos2-1], newlist[pos1-1]
print(newlist)


# Python Program to Swap Two Elements in a List
def swapinglist(newlist, pos1, pos2):
    temp = newlist[pos1-1]
    newlist[pos1 - 1] = newlist[pos2-1]
    newlist[pos2 - 1] = temp
    return newlist


newlist = ["12", "13", "14", "18"]
print(swapinglist(newlist, 1, 3))
