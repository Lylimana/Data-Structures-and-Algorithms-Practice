from random_array import random_array

numbers = random_array(10, 50)

print(numbers)

def quicksort(array): 
    if len(array) <= 1: 
        return array

    pivot = array[0]
    
    less_than_pivot = []
    greater_than_pivot = []    

    for i in array[1:]: 
        if i < pivot: 
            less_than_pivot.append(i) 
        else: 
            greater_than_pivot.append(i)
    print("%15s %1s %15s" % (less_than_pivot, pivot , greater_than_pivot))
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

print(numbers)
print(quicksort(numbers))  