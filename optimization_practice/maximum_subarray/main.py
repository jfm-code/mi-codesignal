# Apply slicing window method
# Calculate the first k numbers, then do a loop, each time remove last number and add a new number
# The max_i is the index of the maximum subarray

def maximum_sum(numbers, k):
    cur_sum = sum(numbers[i] for i in range(k))
    max_sum = cur_sum
    sub_arr_i = 0
    max_i = 0
    for i in range(k, len(numbers)):
        cur_sum = cur_sum + numbers[i] - (numbers[i-k])
        sub_arr_i += 1
        if cur_sum > max_sum:
            max_sum = cur_sum
            max_i = sub_arr_i
    return (max_sum, max_i)