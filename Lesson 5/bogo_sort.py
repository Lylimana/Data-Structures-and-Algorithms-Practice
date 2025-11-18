import random 
import sys
from random_array import random_array

numbers = random_array(5, 100)

print(numbers)

def is_sorted(values): 
    for i in range(len(values)-1): 
        if values[i] > values[i + 1]: 
            return False 
    return True

def bogo_sort(values):
    '''
    Takes random number of times to complete
    '''
    attempts = 0
    while not is_sorted(values): 
        print(attempts)
        random.shuffle(values)
        attempts += 1
    return values 

print(bogo_sort(numbers))