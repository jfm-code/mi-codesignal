# k = number of distinct chars in the substring, for example aacc or aabb, but not abcc
# find the longest substring that satisfy the k condition
# example: acaabcc and k=2
# we have the following substring with k=2 distinct chars: "acaa", "aab", "bcc"
# we see that "acaa" is the longest and therefore we return 4

def solution(s, k):
    hashmap = {}
    left = 0
    right= 0
    max_window = 0
    while right < len(s):
        if s[right] not in hashmap:
            while len(hashmap) >= k:
                hashmap[s[left]] -= 1
                if hashmap[s[left]] == 0:
                    del hashmap[s[left]]
                left += 1
            hashmap[s[right]] = 1
        else:
            hashmap[s[right]] += 1
        max_window = max(max_window, right-left+1)
        # print(s[left], s[right], left, right) #debug statement
        right += 1
    return max_window