# You are given two arrays, arrA and arrB, each containing n integers. 
# Your task is to write a function that returns a pair of distinct indices [i, j] 
# such that the sum of the elements at i and j in array arrA equals the sum of the 
# elements at the same indices in array arrB. 

# If there are multiple valid pairs, return the pair in which i is minimal. 
# If there is still ambiguity, choose the one with minimal j among the latter.

# Consider arrA = [2, 5, 1, 4] and arrB = [3, 6, 3, 2]. In this case, the output should be [2, 3] 
# because arrA[2] + arrA[3] = arrB[2] + arrB[3], i.e., 1 + 4 = 3 + 2.

# Initial solution (complexity = O(n^2)) -> not good
def brute_force_solution(arrA, arrB):
    for i in range(len(arrA)-1):
        for j in range(i+1, len(arrA)):
            if arrA[i]+arrA[j] == arrB[i]+arrB[j]:
                return [i, j]

# Optimize solution, using hashmap to store the difference between each number in A and B (A[i] - B[i])
# We know that 1+4 = 3+2, so 1-3 = 2-4, we can see that 1 with 3 are A[2] with B[2], and 2 with 4 are A[3] with B[3]
# If the differences are opposite numbers (like -2 and 2) then those 4 numbers are the solution

def optimized_solution(arrA, arrB):
    result = []
    hashmap = {}
    for i in range(len(arrA)):
        diff = arrA[i] - arrB[i]
        if -(diff) not in hashmap:
            if diff not in hashmap:
                hashmap[diff] = i
        else:
            result.append([hashmap[-(diff)], i])
    return sorted(result)[0] # sort and return the pair with minimum i and j

# A1 = [1, 2, 3, 4]
# B1 = [2, 1, 1, 4]
A2 = [0, 1, 2, 3, 4, 5, 6]
B2 = [7, 7, 6, 5, 7, 3, 2]
print("Initial solution:", brute_force_solution(A2, B2))
print("Initial solution:", optimized_solution(A2, B2))