# program to find sum and average of list using naive method
test_list = [11, 12, 12, 11, 13]
count = 0
for i in test_list:
    count += i
print(f"the sum of given list is {count} and average of list is {count/len(test_list)}")

# program to find sum and average of given list using sum and average method
test_list = [11, 12, 13, 12, 11]
sum_of_test_list = sum(test_list)
average_test_list = sum_of_test_list/len(test_list)
print(f"sum of list is{sum_of_test_list} and average of test list is {average_test_list}")

# program to find sum and average of given list Using sum() and statistics.mean()
import statistics
test_list = [11, 10 ,12, 15, 13]
sum_of_test_list = sum(test_list)
average_test_list = statistics.mean(test_list)
print(f"sum is {sum_of_test_list} and average is {average_test_list}")


#  using NumPy module functions sum() and average()
import  numpy


test_list = [11, 13, 14, 15]
sum_of_list = numpy.sum(test_list)
average_test_list = numpy.average(test_list)
print(f"sum is {sum_of_list} and average is {average_test_list}")


# using reduce and lamda function


from functools import reduce

L = [4, 5, 1, 2, 9, 7, 10, 8]

# Finding the sum using reduce() and lambda
count = reduce(lambda x, y: x + y, L)

# divide the total elements by number of elements
avg = count / len(L)

print("sum = ", count)
print("average = ", avg)

# using only the built-in functions sum() and len()
testing_list = [11, 12, 13, 14]
sum_of_testing_list = sum(testing_list)
average_of_testing_list = sum_of_testing_list/len(testing_list)
print(f"sum is {sum_of_testing_list} and average is {average_of_testing_list}")
