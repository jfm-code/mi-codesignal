# Write a Python function to count how many 3x3 submatrices in a given matrix have 'E's in all four corners
# One such matrix is:
# E P E
# P E P
# E P E

def countSubmatricesWithE(board):
    rows, cols = len(board), len(board[0])
    if rows < 3 or cols < 3:
        return 0
    count = 0
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            if ((board[row-1][col-1] == 'E') and # top left
                (board[row+1][col-1] == 'E') and # down left
                (board[row-1][col+1] == 'E') and # top right
                (board[row+1][col+1] == 'E')): # down right
                count += 1
    return count
    
    
sample_board = [
    ['E', 'P', 'E', 'P'],
    ['P', 'E', 'P', 'E'],
    ['E', 'P', 'E', 'P'],
    ['P', 'E', 'P', 'E']
]

print(countSubmatricesWithE(sample_board))