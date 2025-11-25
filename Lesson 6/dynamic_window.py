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