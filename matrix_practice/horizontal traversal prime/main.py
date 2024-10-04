# Horizontal zigzag traverse and find prime number
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
# Traversal: [1, 2, 3, 6, 5, 4, 7, 8, 9]
# Prime numbers and its indexes: {2: 2, 3: 3, 5: 5, 7: 7}

import math

def is_prime(n):
    # number 1 is not prime
    if n == 1: return False
    
    # number 2 is prime, this is an exception, cause all even numbers are not prime, except 2
    elif n == 2: return True
    
    # even numbers are not prime
    elif n % 2 == 0: return False
    
    # prime numbers must be bigger than 2
    else:
        for divisor in range(3, int(math.sqrt(n))+1, 2):
            if n % divisor == 0:
                return False
        return True
        # explanation:
        # - start from 3 because we already check for even number, and any number can divide by 1
        # - use square root because divisors come in pairs, so if we check from 3-> sqrt(n) then we already count for the pair from sqrt(n) -> n
        # - step is 2 cause we already check for even number, this will increase efficiency
        

def zigzag_traverse_and_primes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    r = c = 0
    result = {}
    order = []
    dir = 'right'
    for _ in range(rows*cols):
        if 0 <= r < rows and 0 <= c < cols:
            order.append(matrix[r][c])
        if dir == 'right':
            if c < cols-1:
                c += 1
            else:
                dir = 'left'
                r += 1
        else:
            if c > 0:
                c -= 1
            else:
                dir = 'right'
                r += 1
    
    for i, n in enumerate(order, start=1):
        if is_prime(n):
            result[i] = n
    return result
