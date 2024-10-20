# X = [4, 12, 9, 20]
# Y = [10, 20, 40, 50]
# Output: [10, 40, 50, 50]
# Y should be at least as long as X

# For Y[0] (=10), the half is 5. The function identifies X[0] (=4) as the closest value. As X[0] has been selected, it includes the corresponding Y[0] value (10) in the new array.
# Next, for Y[1] (=20), the half is 10. The function identifies X[2] (=9) as the closest value. As X[2] has been selected, it includes the corresponding Y[2] value (40) in the new array. Now, the new array is [10, 40].

# This is pretty similar to the closest_double_number.py problem in optimization_practice, but this time we'll need
# to use 2-pointer technique because we're working on 2 arrays at the same time, so we're using 1 pointer for each
# We also need to sort 2 arrays and leverage the tuple type

def solution(X, Y):
    sorted_X = sorted((val, index) for index, val in enumerate(X))
    sorted_Y = sorted((val, index) for index, val in enumerate(Y))

    x_pointer = 0
    y_pointer = 0
    result = [0] * len(Y)
    while y_pointer < len(Y):
        target = sorted_Y[y_pointer][0] / 2
        while x_pointer < len(X)-1 and abs(target - sorted_X[x_pointer + 1][0]) < abs(target - sorted_X[x_pointer][0]):
            x_pointer += 1
        result[sorted_Y[y_pointer][1]] = Y[sorted_X[x_pointer][1]]
        y_pointer += 1
    return result
    