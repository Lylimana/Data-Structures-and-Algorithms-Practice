from random_array import random_array

numbers = random_array(10, 50)

print(numbers)

def merge_sort(array): 
    if len(array) <= 1: 
        return array 
    
    mid_point = len(array)//2 
    
    sorted = []
    i = 0
    j = 0
    left = array[mid_point:]
    right = array[:mid_point]
    
    while len(left) > i and len(right) > j: 
        if left[i] < right[i]: 
            sorted.append(left[i])
            i += 1
        else: 
            sorted.append(right[j])
            j += 1
            
    while len(left) > i: 
        sorted.append(left[i])
        i += 1

    while len(right) > j: 
        sorted.append(right[j])
        j += 1
    
    
    return sorted


print(merge_sort(numbers))