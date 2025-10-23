def find_x(array, target): 
    if target in array: 
        print(str(target) + " is in the array.")
        
def find_x_2(array, target): 
    for i in array: 
        if i == target: 
            print(str(target) + " is in the array.")
            break 