# Array A = [10, 20, 30, 40, 50] 
# Array B = [7, 5, 1, 2, 4]

# For B[0] = 7, the closest number in Array B is 5 at index 1. Hence, C[0] = A[1] = 20.
# For B[1] = 5, the closest number in Array B is 4 at index 4. Thus, C[1] = A[4] = 50.
# For B[2] = 1, the closest number in Array B is 2 at index 3. Hence, C[2] = A[3] = 40.
# For B[3] = 2, the closest number in Array B is 1 at index 2. So, C[3] = A[2] = 30.
# Lastly, for B[4] = 4, the closest number in Array B is 5 at index 1. We have C[4] = A[1] = 20.

# Output is Array C = [20, 50, 40, 30, 20]

def optimizedReplace(A, B):
    if len(A) == len(B) == 1:
        return [1]
    
    result = [0] * len(A)
    
    # Put B values and indexes in tuples, then sort them
    sortB = sorted((val, i) for i, val in enumerate(B))
    
    # Find the closest number
    result[sortB[0][1]] = A[sortB[1][1]] # edge case, first element
    result[sortB[-1][1]] = A[sortB[-2][1]] # edge case, last element
    
    for i in range(1, len(sortB)-1):
        abs_prev = abs(sortB[i][0] - sortB[i-1][0])
        abs_next = abs(sortB[i][0] - sortB[i+1][0])
        if abs_prev < abs_next:
            result[sortB[i][1]] = A[sortB[i-1][1]]
        else:
            result[sortB[i][1]] = A[sortB[i+1][1]]

    return result