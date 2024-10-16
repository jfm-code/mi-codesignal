# This problem can also be used to find pairs that their sum equals a target number, not just 0
# We will sort this array first, then implement 2 pointer technique (move the pointer according to the current sum)

def find_choc_pairs(sweetness):
    sweetness = sorted(sweetness)
    left = 0
    right = len(sweetness) - 1
    result = []

    while left < right:
        cur_sum = sweetness[left] + sweetness[right]
        if cur_sum == 0: # if sum == target -> move both pointers
            pair = (sweetness[right], sweetness[left]) # insert pair in decreasing order directly
            result.append(pair)
            left += 1
            right -= 1
        elif cur_sum > 0: # if sum > target -> move right pointer
            right -= 1
        else: # if sum < target -> move left pointer
            left += 1

    # sorting all pairs by the first element in each pair 
    result = sorted(result, key=lambda pair : pair[0])

    return result