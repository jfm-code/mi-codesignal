def reflectOverSecondaryDiagonal(matrix):
    size = len(matrix)
    new_matrix = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size-i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[size-1-j][size-1-i]
            matrix[size-1-j][size-1-i] = temp
            # print("swapping:", matrix[i][j], matrix[size-1-j][size-1-i])
            
    return matrix

# Example square matrix to reflect over the secondary diagonal
square_matrix = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

# TODO: Call the function on square_matrix and store the result in transformed_matrix.
print(reflectOverSecondaryDiagonal(square_matrix))
# Output should be:
# [
#  [9, 6, 3],
#  [8, 5, 2],
#  [7, 4, 1]
# ]

# The first approach can be transpose the matrix first, then in each row reverse order, then reverse the rows
# But this approach involves too many step, theres a better way
# Final approach is to figure out the relationship between indexes
# [0][0] -> [2][2]
# [0][1] -> [1][2]
# [0][2] -> [0][2]
# then
# [1][0] -> [2][1]
# [1][1] -> [1][1]
# be careful not to swap 2 times
