# The first 2 input matrices are matrix A and B
# The last input matrix is the start and end ranges for rows and columns that will be extracted
# It follows (start_row, end_row, start_column, end_column)

def solution(matrix_A, matrix_B, submatrix_coords):
    # get the start/end row/col for each matrix
    start_RA, end_RA = submatrix_coords[0][0], submatrix_coords[0][1]
    start_CA, end_CA = submatrix_coords[0][2], submatrix_coords[0][3]
    start_RB, end_RB = submatrix_coords[1][0], submatrix_coords[1][1]
    start_CB, end_CB = submatrix_coords[1][2], submatrix_coords[1][3]
    
    rows = end_RA - start_RA + 1
    
    sub_A = []
    sub_B = []
    # extract the submatrices based on the coords
    for i in range(rows):
        sub_A.append(matrix_A[start_RA-1:end_RA][i][start_CA-1:end_CA])
        sub_B.append(matrix_B[start_RB-1:end_RB][i][start_CB-1:end_CB])
    # print(sub_A) #DEBUG
    # print(sub_B) #DEBUG
    
    # concatenate matrices
    # using zip() to iterate through 2 matrices at the same time
    result = []
    temp = []
    for mat_A, mat_B in zip(sub_A, sub_B):
        for a, b in zip(mat_A, mat_B):
            temp += [a,b]
        result.append(temp)
        temp = []
    return result