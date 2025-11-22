def hash_map(data): 
    '''
    Run time: O(1)
    '''
    hm = {}
    
    for target in data: 
        if target not in hm: 
            hm[target] = 1 
        else: 
            hm[target] += 1  
            
    return hm
            
            
data = [1,2,3,4,5,6,7,8,9,10]

print(hash_map(data))