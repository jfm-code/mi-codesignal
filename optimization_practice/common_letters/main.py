# Implement the most optimal way to find the common letters between a string and a list of characters
# We can use the "in" method, but using set intersection is faster

def solution(s, letters):
    s = set(s)
    letters = set(letters)
    result = s & letters
    return sorted(result)
    
s = "a"*500
letters = ['a', 'b', 'c']
print(solution(s, letters))