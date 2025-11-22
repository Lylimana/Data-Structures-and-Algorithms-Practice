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

data = [2, 7,  11, 15]

target = 9 

def two_sum (arr: list[int], target: int) -> list[int]: 
    num_to_index = {}
    
    for i, num in enumerate(arr): 
        complement = target - num 
        if complement in num_to_index: 
            return [num_to_index[complement], i]
        num_to_index[num] = i
        return []
    
if __name__ == "__main__": 
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = two_sum(arr, target)
    print(" ".join(map(str, res))) 