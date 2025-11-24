def two_pointers(s: str): 
    '''
    Palindrome
    
    .isalnum checks if data is letters or numbers. if it is anything else, it is set as false
    '''
    l, r = 0, len(s) - 1
    while l < r: 
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower(): 
            return False
        l += 1
        r -= 1   
    return True

if __name__ == "__main__": 
    string1 = 'TACOCAT'
    string2 = 'DUhhhhhhhhhhhhhh'
    print(two_pointers(string1))
    print(two_pointers(string2))