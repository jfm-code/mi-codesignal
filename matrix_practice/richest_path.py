def trek_path(elevation_map, start_x, start_y):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    path = [elevation_map[start_x][start_y]] # append the starting point to the path
    rows, cols = len(elevation_map), len(elevation_map[0])
    
    while True:
        current_height = path[-1]
        # we need the last element of path because the last will be the current highest elevation value
        
        possible_next_moves = []
        for dx, dy in directions:
            new_x, new_y = start_x + dx, start_y + dy
            if (0 <= new_x < rows) and (0 <= new_y < cols):
                if elevation_map[new_x][new_y] > current_height:
                    possible_next_moves.append((new_x, new_y))
        
        # use the lambda key for max() function
        # lambda creates an anonymous function
        # move is the parameter for the lambda function, representing each element in possible_moves
        if not possible_next_moves:
            break
        else:
            next_move_index = max(possible_next_moves, key=lambda move: elevation_map[move[0]][move[1]])
            path.append(elevation_map[next_move_index[0]][next_move_index[1]])
            start_x = next_move_index[0]
            start_y = next_move_index[1]
    
    return path

mountain = [
    [1, 2, 3],
    [2, 3, 4],
    [3, 5, 6]
]
print(trek_path(mountain, 1, 1))
# the path would be [3, 5, 6]
# from value 3 we can go to 4 or 5, but 5 is bigger, so choose 5