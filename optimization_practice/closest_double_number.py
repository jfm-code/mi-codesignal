# Given these 2 arrays
# A = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
# B = [4, 12, 3, 9, 6, 1, 5, 8, 37, 25, 100]

# We find the closest number for each number of B by the following rule
    # The first item in B is 4 at index=0. Double of this number is 8. 
    # The closest number to 8 in array B is 8 which is at index=7. 
    # The number at the same index in array A is 80, so we add 80 to our new array.

    # The second item in B is 12 at index=1. Double of this number is 24. 
    # The closest number to 24 in B is 25 which is at index=9. Corresponding index in A has the number 100. 
    # So, we add 100 to our new array.

# Output should be: [80, 100, 50, 20, 20, 60, 40, 20, 110, 90, 110]

def find_closest(arrA, arrB):
    # sort B array into tuple(value, index) with values in ascending order
    sorted_B = sorted((val, index) for index, val in enumerate(arrB))
    print("array B after sorting:", sorted_B)
    result = [0]*len(arrA)
    for tuple_i in range(len(sorted_B)):
        closest_tuple_i = tuple_i
        target = sorted_B[tuple_i][0] * 2
        # if the next tuple has value < target, move to that tuple (move right)
        # so that there are higher chance of reaching a closer value
        while closest_tuple_i < len(arrB)-1 and sorted_B[closest_tuple_i + 1][0] < target:
            closest_tuple_i += 1
        # compare the current tuple with the next tuple to see which one has a closer value to the target
        if closest_tuple_i < len(arrB)-1 and abs(target - sorted_B[closest_tuple_i + 1][0]) < abs(target - sorted_B[closest_tuple_i][0]):
            closest_tuple_i += 1

        # find the value in arrA and put it in the result array
        result[sorted_B[tuple_i][1]] = arrA[sorted_B[closest_tuple_i][1]]

    return result

A = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
B = [4, 12, 3, 9, 6, 1, 5, 8, 37, 25, 100]
print("output:", find_closest(A, B))
