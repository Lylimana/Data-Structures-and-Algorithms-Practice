from random_array import random_array

numbers = random_array(10, 50)

print(numbers)

def index_of_min(array): 
    min_index = 0
    for i in range(len(array)): 
        if array[i] < array[min_index]: 
            min_index = i 
    return min_index

def quicksort(array): 
    if  len(array) <= 1: 
        return array

    pivot = array[0]
    
    less_than_pivot = []
    greater_than_pivot = []    

    for i in array: 
        if i < pivot: 
            less_than_pivot.append(array.pop(i)) 
        else: 
            greater_than_pivot.append(array.pop(i))
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

print(quicksort(numbers))  