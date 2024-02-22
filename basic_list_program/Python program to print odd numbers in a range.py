# program to print all odd numbers in range
def odd_numbers(start, end):
    res = []
    for i in range(start, end + 1):
        if i % 2 != 0:
            res.append(i)
        else:
            pass
    return res


print(f"the all odd numbers in list is {odd_numbers(1, 19)}")

# program to find all odd numbers in list using pass method
def odd(start, end):
    result = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            pass
        else:
            result.append(i)
    return result


print(f"all odd numbers in lists are {odd(2, 14)}")

# using list comprehension
start = 1
end = 6
result_list = [i for i in range(start, end + 1) if i % 2 != 0]
print(f"the all odd numbers in lists are {result_list}")
