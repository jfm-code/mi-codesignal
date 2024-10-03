# Traverse diagonally, order of output numbers is [1, -2, 5, -9, -6, 3, -4, 7, 10, -11, 8, 12]
# Return the indexes of negative numbers, so final output is [(1, 2), (3, 1), (2, 2), (1, 4), (3, 3)]
# which are indexes of [-2, -9, -6, -4, -11]
# arr =  [[ 1,  -2,  3, -4],
#         [ 5,  -6,  7,  8],
#         [-9, 10, -11, 12]]

# The logic for the if-else conditions is quite tricky
# Try to focus on cases where the direction changes

def solution(matrix):
    rows, cols = len(matrix), len(matrix[0])
    direction = 'up'
    r, c = 0, 0
    order = []
    result = []
    for _ in range(rows * cols):
        if 0 <= r < rows and 0 <= c < cols:
            order.append(matrix[r][c]) # No need but useful to debug to see the complete traversal
            if matrix[r][c] < 0:
                result.append((r+1, c+1))
        
        if direction == 'up':
            # going up, reach the first row -> move right & change direction
            if r == 0:
                c += 1
                direction = 'down'
            # going up, reach the last col -> move down & change direction
            elif c == cols-1:
                r += 1
                direction = 'down'
            # other cases -> move up-right & no change direction
            else:
                r -= 1
                c += 1
                
        else:
            # going down, reach first col -> move down & change direction
            if c == 0:
                r += 1
                direction = 'up'
            # going down, reach last row -> move right & change direction
            elif r == rows-1:
                c += 1
                direction = 'up'
            # other cases -> move down-left & no change direction
            else:
                r += 1
                c -= 1
    
    return result