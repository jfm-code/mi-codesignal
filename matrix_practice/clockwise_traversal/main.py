# Perform a spiral traversal and return the 1-indexes of vowels
# Be careful of the edge cases

# arr= [['a', 'b', 'c', 'd'],
#       ['e', 'f', 'g', 'h'],
#       ['i', 'j', 'k', 'l']]
# output = ['a', 'b', 'c', 'd', 'h', 'l', 'k', 'j', 'i', 'e', 'f', 'g']
# index = [1, 9, 10] (of a, i, e)

def spiral_traverse_and_vowels(grid):
    rows, cols = len(grid), len(grid[0])
    order = []
    result = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    r = c = 0
    start_r = start_c = 0
    
    # edge cases (when rows=1 or cols=1)
    if rows == 1:
        for y in range(cols):
            order.append(grid[r][y])
    elif cols == 1:
        for i in range(rows):
            order.append(grid[i][c])
    # other cases
    else:
        for _ in range(rows * cols):
            # print(r,c) # DEBUG
            if 0 <= r < rows and 0 <= c < cols:
                order.append(grid[r][c])
            
            if r == start_r and c < cols-1:
                # move right
                c += 1
            elif c == start_c and r > start_r:
                # move up
                if r-1 == start_r and c < cols-start_c-1: # condition to skip the previous row & col
                    start_r += 1
                    start_c += 1
                    rows -= 1
                    cols -= 1
                    c += 1
                else:
                    r -= 1
            elif c == cols-1 and r < rows-1:
                # move down
                r += 1
            elif r == rows-1 and c > start_c:
                # move left
                c -= 1
        
    for i, c in enumerate(order, start=1):
        if c in vowels:
            result.append(i)

    # print(order, result) # DEBUG
    return result