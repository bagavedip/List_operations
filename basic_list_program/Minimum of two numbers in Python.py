# find the minimum of two numbers in python program using if conditions
def minimum(a, b):
    if a < b:
        return f"a={a} is minimum"
    elif a > b:
        return f"b={b} is minimum"
    else:
        return f"a={a} and b={b} both are equals."


a = 2
b = 7
minimum(a, b)


# find the minimum of two numbers in python program using min() method
a = 4
b = 7
result = min(a, b)
print(f"minimum is{result}")


# find the minimum of two numbers in python program using sorting method
a = 5
b = 9
result = [a, b]
result.sort()
print(f"minimum is {result[-1]}")



