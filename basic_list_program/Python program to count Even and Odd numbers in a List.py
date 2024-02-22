# program to count even and odd numbers in list


def even_odd(test_list):
    even = []
    odd = []
    for i in test_list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return f"even={len(even)} and odd={len(odd)}"


test_list = [1, 2, 3, 4, 7, 5, 6, 3]
print(even_odd(test_list))

# program to find even and odd numbers count using list comprehension
test_list = [11, 10, 12, 13, 1, 2]
result = [i for i in test_list if i % 2 == 1]
even = len(test_list) - len(result)
print(f"the even count of element are {even} and odd count of element are {len(result)}")



