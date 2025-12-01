def binary_search(list: list, target: int):
    left, right = 0, len(list) - 1
    
    first_true_index = -1
    while left <= right: 
        midpoint = (left+right)//2
        if target == list[midpoint]: 
            first_true_index = midpoint
            return first_true_index
        elif  target < list[midpoint]:
            right = midpoint - 1
        else: 
            left = midpoint + 1
    return first_true_index
    
if __name__ == "__main__": 
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    target = 15
    
    print(binary_search(list, target))