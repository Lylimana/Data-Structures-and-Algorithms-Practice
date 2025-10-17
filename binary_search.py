from number_array import create_number_list
from verify import verify

numbers_100 = []

numbers_100 = create_number_list(numbers_100, 100)

# Binary Search
def binary_search(list, target): 
    first = 0
    last = len(list)-1
    
    while first <= last: 
        midpoint = (first + last)//2 
        
        if list[midpoint] == target: 
            return midpoint 
        elif list[midpoint] < target: 
            first = midpoint + 1 
        else:
            last = midpoint - 1 
    return None 

results = binary_search(numbers_100, 40)

verify(results)