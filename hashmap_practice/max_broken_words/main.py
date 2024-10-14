# The goal is to figure out which single character, if removed from the string, 
# would "break" / affect the most words in that string
# For example if we remove 'l' in "Hello, world", there are 2 words being affected
# Same for 'o', when we remove that character, also 2 words being affected
# But we return only the character that appears first, so return 'l' instead of 'o'
# Attention, in strings like "Winners never quit and quitters never win.", the letter 'n' affects only
# 4 strings, not 5, cause "never" appears twice

def solution(s):
    words = set(s.split()) # use set to prevent duplicate words
    characters = sorted(set(s)) # without the sorted(), the order of the set will vary each time run

    hashmap = {}
    for c in characters:
        for word in words:
            if c in word:
                hashmap[c] = hashmap.get(c, 0) + 1
                
    first_index = float('inf')
    words_affected = max(hashmap.values())
    for key, val in hashmap.items():
        if val == words_affected:
            first_index = min(first_index, s.find(key))
    
    return (s[first_index], words_affected)
