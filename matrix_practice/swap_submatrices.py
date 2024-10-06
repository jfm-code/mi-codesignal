def submatrix_swap(matrix, coord_S1, coord_S2):
    old_sub = matrix[coord_S1[0] : coord_S1[1]]
    new_sub = matrix[coord_S2[0] : coord_S2[1]]

    for old, new in zip(old_sub, new_sub):
        temp = old[coord_S1[2] : coord_S1[3]]
        old[coord_S1[2] : coord_S1[3]] = new[coord_S2[2] : coord_S2[3]]
        new[coord_S2[2] : coord_S2[3]] = temp
        # print(matrix)

    return matrix
    
    
input_m =  [[1, 2, 3, 4, 5], 
            [6, 7, 8, 9, 10], 
            [11, 12, 13, 14, 15], 
            [16, 17, 18, 19, 20], 
            [21, 22, 23, 24, 25]]
            
output_m = [[16, 17, 3, 4, 5], 
            [21, 22, 8, 9, 10], 
            [11, 12, 13, 14, 15], 
            [1, 2, 18, 19, 20], 
            [6, 7, 23, 24, 25]]

# the coords of 2 submatrices in input_m
coord_S1 = [0, 2, 0, 2] # from row 0-1, col 0-1
coord_S2 = [3, 5, 0, 2] # from row 3-4, col 0-1

print(submatrix_swap(input_m, coord_S1, coord_S2))