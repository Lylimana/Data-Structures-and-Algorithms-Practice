import random

def random_list_generator(list_len, list_range): 
    '''
    Creates an array/list with random numbers 
    
    Takes a number for list length and list range 
    
    Outputs array with random numbers between 0 and list range of list length size
    '''
    l = []
    
    for i in range(list_len): 
        l.append(random.randrange(0, list_range))
        
    return l