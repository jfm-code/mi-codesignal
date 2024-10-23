# TODO: implement a function that finds a pair of numbers whose sum equals the target
# We can use a nested loop, but that will result in a O(n^2)
# Use a hashmap and think about complement number instead
# A thing to remember about this problem is that we need to return the pair with the first number has lowest index

def solution(arr, target):
    hashmap = {}
    for i in range(len(arr)):
        if arr[i] not in hashmap:
            complement = target - arr[i]
            if complement not in hashmap:
                hashmap[complement] = i
        else:
            complement_i = hashmap[arr[i]]
            if i < complement_i:
                return [arr[i], arr[complement_i]]
            else:
                return [arr[complement_i], arr[i]]
    return []

print(solution([2, 13, 4, 7, 5, 15], 9))