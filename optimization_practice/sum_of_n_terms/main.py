# The goal is to calculate the sum from number a to number b, apply maths

def sum_with_formula(n):
    return (n*(n+1)) // 2

def solution(a, b):
    if a == b:
        return a
    elif a == 1 or b == 1: 
        # if calulate the sum from 1, we can use a math formula n*(n+1)/2
        return sum_with_formula(max(a, b))
    else: 
        # if the calculate the sum from a mid point, like from 12 to 50, then calculate the sum from 1 to 50,
        # then minus the sum from 1 to 12, also add 12 back cause we want 12 inclusively 
        if a > b: 
            big_n = a
            small_n = b
        else:
            big_n = b
            small_n = a
        return sum_with_formula(big_n) - sum_with_formula(small_n) + small_n