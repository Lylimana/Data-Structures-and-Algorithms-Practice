from number_array import create_number_list
from verify import verify_true_false

numbers_200 = []

numbers_200 = create_number_list(numbers_200, 200)

def recursive_binary_search(list, target):
    if len(list) == 0: 
        return False
    else: 
        midpoint = (len(list))//2
        
        if list[midpoint] == target: 
            return True
        else: 
            if list[midpoint] < target: 
                return recursive_binary_search(list[midpoint +1:], target)
            else: 
                return recursive_binary_search(list[:midpoint], target)
            
result = recursive_binary_search(numbers_200, 149)

verify_true_false(result)