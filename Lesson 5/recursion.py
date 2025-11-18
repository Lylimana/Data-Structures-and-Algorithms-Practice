from random_array import random_array

def sum(numbers): 
    sum = 0 
    for number in numbers: 
        sum += number
    return sum 

numbers = random_array(5, 100)

print(numbers)

print(sum(numbers))


def sum_recursion(numbers): 
    if not numbers:
        return 0
    print("Calling sum(%s)" % numbers[1:])
    remaining_sum = sum_recursion(numbers[1:])
    print("call to sum(%s) returning %d + %d" % (numbers, numbers[0], remaining_sum))
    return numbers[0] + remaining_sum

print(sum_recursion(numbers))    