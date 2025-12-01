'''
def sliding_window_dynamic(input):
    initialize windows, ans 
    left = 0
    for right in range(len(input)): 
        append input[right] to window
        while invalid(window):
            remove inpt[left] from window 
            left += 1
        ans = max(ans, window)
    return ans
'''
from collections import defaultdict

def longest_substring_withot_repeating_characters(s: str) -> int: 
    longest = 0 # Tracks maximum substing length seen so far 
    l = 0 # Start of sliding window
    
    counter: dict[str, int] = defaultdict(int) # Keep track of the number of times a number appears in window
    for r in range(len(s)):
        counter[s[r]] += 1
        while counter[s[r]] >1: 
            counter[s[l]] -= 1
            l += 1
        longest = max(longest, r - l + 1)
    return longest 


if __name__ == "__main__": 
    s = 'Hello my name is Miguel Manalili'
    
    print(longest_substring_withot_repeating_characters(s))