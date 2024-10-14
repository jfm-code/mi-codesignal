# The goal is to choose an integer k from the array, so that when we remove all k's occurrence in the array,
# we'll get the subarrays with the minimal length
# example: [1, 2, 2, 3, 1, 4, 4, 4, 1, 2, 5]
# if we remove number 2, the subarrays are [1], [3, 1, 4, 4, 4, 1], [5] -> longest subarray length is 6
# but if we remove number 1, the subarrays are [2, 2, 3], [4, 4, 4], [2, 5] -> longest subarray length is 3
# so we should return 1 instead of 2

def minimal_block(arr):
    max_block_len = {}
    last_occurence = {}

    # calculate the maximum of the block from the beginning/last occured number to the current number
    for i, num in enumerate(arr):
        if num not in max_block_len:
            max_block_len[num] = i
        else:
            cur_block_len = i - last_occurence[num] - 1
            max_block_len[num] = max(max_block_len[num], cur_block_len)
        # update the index of the last occured number at the end (not at the beginning)
        last_occurence[num] = i

    # don't forget the length of the block from the last occured number to the end of the array
    for num, last_i in last_occurence.items():
        tail_block_len = len(arr) - last_i - 1
        max_block_len[num] = max(max_block_len[num], tail_block_len)
    
    num_with_min_len_block = min(max_block_len, key=max_block_len.get) # return the key instead of value
    return num_with_min_len_block

print(minimal_block([1, 2, 2, 3, 1, 4, 4, 4, 1, 2, 5]))