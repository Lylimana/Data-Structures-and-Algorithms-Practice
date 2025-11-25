'''
Example: 

def sliding_window_fixed(input, window_size): 
    ans = window = input[0:window_size]
    for right in range(window_size, len(input)):
        left = right - window_size 
        remove input[left] from window
        append input[right] to window
        ans = optima(ans, window)
    return ans
'''

def sliding_window_fixed(nums: list[int], k: int) -> int:
    window_sum = 0 
    for i in range(k):
        window_sum += nums[i]
    largest = window_sum
    for right in range(k, len(nums)):
        left = right - k
        window_sum -= nums[left]
        window_sum += nums[right]
        largest = max(largest, window_sum)
    return largest

def sliding_window_fixed_words(word: str, target: str):
    target_list = list(target)
    word_arr = []
    for i in range(len(target)): 
        word_arr.append(word[i])
    if word_arr == target_list: 
        return word_arr
    for right in range(len(target), len(word)):
        word_arr.pop(0)
        word_arr.append(word[right])
        if word_arr == target_list: 
            return word_arr


if __name__ == '__main__': 
    nums = [1,2,3,7,4,1]
    k = 3
    
    # print(sliding_window_fixed(nums, k))
    
    word = "orange"
    target = "ran"
    
    print(sliding_window_fixed_words(word, target))
    
    word2 = "Shamalamadingdong"
    target2 = "ding"
    
    print(sliding_window_fixed_words(word2, target2))