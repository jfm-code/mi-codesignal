# The goal is to find the adjacent cell (including diagonals) with the highest value that is greater than the current cell's value.
def find_next_uphill(grid, position):
    row, col = position
    # Up, down, left, right, top-left, top-right, down-left, down-right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    next_val = grid[row][col]
    
    for dr, dc in directions:
        new_r, new_c = row + dr, col + dc
        if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] > next_val:
            next_val = grid[new_r][new_c]
    if next_val != grid[row][col]:
        return next_val 
    else:
        return None

# Example usage:
trail_grid =[[1, 2, 3], 
            [6, 5, 8], 
            [7, 4, 9]]
start_position = (1, 1)
# Output should be 9
print(find_next_uphill(trail_grid, start_position))