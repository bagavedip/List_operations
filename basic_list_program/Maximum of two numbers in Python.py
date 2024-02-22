# Find Maximum in two numbers using if condition.
a = 4
b = 2
if a > b:
    print(f"a={a} is maximum")
elif b > a:
    print(f"b={b} is maximum in two numbers")
else:
    print(f"a={a} and b={b} both are equal")


# Find Maximum in two numbers using max() function.
def maximum(a, b):
    number = max(a, b)
    return number


a = 4
b = 3
print(f"maximum is :{maximum(a, b)}")

# Find Maximum in two numbers using sorting method.
a = 2
b = 6
numbers = [a, b]
numbers.sort()
print(f"maximum number is:{numbers[-1]}")

