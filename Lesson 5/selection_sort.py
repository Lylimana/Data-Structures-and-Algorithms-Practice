from random_array import random_array

def selection_sort(array): 
    sorted = []

    # while len(sorted) < len(array): 
    #     pointer = 0
    #     current = pointer
    #     next = pointer+1
        
    #     target = None
        
    #     if array[current] > array[next]: 
    #         target = array[next]
    #         pointer += 1
    #     else: 
    #         target = array[current]
    #         sorted.append(target)
    
    # return sorted
    print("%-25s %-25s" % (array, sorted))
    for i in range(0, len(array)): 
        index_to_move = index_of_min(array)
        sorted.append(array.pop(index_to_move))
        print("%-25s %-25s" % (array, sorted))
    return sorted 

def index_of_min(array):
    min_index = 0
    for i in range(1, len(array)):
        if array[i] < array[min_index]:
            min_index = i
    return min_index
            
random_array = random_array(5, 30)

print(selection_sort(random_array))           
