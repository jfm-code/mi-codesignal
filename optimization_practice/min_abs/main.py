# Implement the function to find minimum absolute difference among all pairs.
# We can use 2 for-loops to compare all pairs, but to maximize efficiency, let's sort the list first then compare only 2 numbers at a time, so we'll only loop through the list once

def solution(nums):
    # edge case
    if len(nums) == 1:
        return 0
    # other cases
    nums.sort()
    cur_abs = 0
    min_abs = float('inf') # set min_abs to a really big number
    for i in range(1, len(nums)):
        cur_abs = abs(nums[i]-nums[i-1])
        min_abs = min(cur_abs, min_abs)
    return min_abs
    
