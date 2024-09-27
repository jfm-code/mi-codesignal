def evaluate_move(board):
    # TODO: Check if a move to the given cell is possible; write a condition to check if the cell is empty.
    # Also, check if at least one neighboring cell is empty (not diagonally).
    rows = len(board)
    cols = len(board[0])
    indexes = []
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 'E':
                if ((row > 0 and board[row - 1][col] == 'E') or # UP
                    (row < rows-1 and board[row + 1][col] == 'E') or # DOWN
                    (col > 0 and board[row][col - 1] == 'E') or # LEFT
                    (col < cols-1 and board[row][col + 1] == 'E')):
                    indexes.append((row, col))
    return indexes 

# Assuming a constant 2D array representing a board
board = [
    ['P', 'E', 'E', 'P'],
    ['E', 'P', 'E', 'P'],
    ['P', 'E', 'P', 'P'],
    ['P', 'E', 'P', 'E']
]

print(evaluate_move(board))

# TODO: Write a list comprehension to find all valid move positions.
# If we want to check if the cell at position (0, 1) is a valid move, we need to:
# Ensure the cell (0, 1) is empty ('E').
# Check if at least one of its neighboring cells (up, down, left, right) is also empty.