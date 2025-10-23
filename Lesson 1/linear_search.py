from number_array import create_number_list
from verify import verify

numbers_100 = []

numbers_100 = create_number_list(numbers_100, 100)


# Linear Search 
def linear_search(list, target): 
     """ 
     Returns te index position of te target if found, else returns None
     """
     
     for i in range(0, len(list)):
         if list [i] == target: 
             return i 
     return None 
 
        
results = linear_search(numbers_100, 110)

verify(results)