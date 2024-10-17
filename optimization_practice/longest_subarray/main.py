# Apply slicing window method
# Move the right pointer to expand the window and add the current element to the sum.
# If the sum exceeds k, move the left pointer to reduce the sum until it's less than or equal to k.

def get_longest_subarray(array, k):
    right = 0
    left = 0
    cur_sum = 0
    start_i = -1
    max_window_len = 0
    
    while right < len(array):
        cur_sum += array[right]
        right += 1
        
        while cur_sum > k and left <= right:
            cur_sum -= array[left]
            left += 1
            
        if cur_sum == k:
            if right-left + 1 > max_window_len:
                max_window_len = right-left + 1
                start_i = left
    
    return array[start_i : start_i+max_window_len-1]