import random

def random_array(list_len, list_range): 
    '''
    Creates random array
    
    Runs in O(n)
    '''
    array = []
    
    for i in range(list_len): 
        array.append(random.randint(0, list_range))
    return array
