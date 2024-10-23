# Identify exactly four numbers in the list that their sum equal the target number.
# If no such quad exists, the function should return an empty list.
# Example: [5, 15, 2, 7, 8, 4], target=24
# Output: [5, 7, 4, 8]
# The brute force way is to go through every quadruple, which can make the complexity O(n^4)
# But if we use map then it can be O(n^2)

def find_quad_sum(target_sum, numbers):
    # find the sum of every pairs, store in a map
    # the key will be the sum, value is the array of 2 number's indexes that sum up to the key
    sum_map = {}
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            key = numbers[i] + numbers[j]
            if key not in sum_map:
                sum_map[key] = [(i, j)]
            else:
                sum_map[key].append((i, j))

    for x in range(len(numbers)-1):
        for y in range(x+1, len(numbers)):
            difference = target_sum - (numbers[x] + numbers[y])
            if difference in sum_map:
                for pair in sum_map[difference]:
                    i = pair[0]
                    j = pair[1]
                    if i != x and i != y and j != x and j != y:
                        return [numbers[x], numbers[y], numbers[i], numbers[j]]


print(find_quad_sum(24, [5, 15, 2, 7, 8, 4]))