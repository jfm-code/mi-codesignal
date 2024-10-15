# In the list ['dog', 'cat', 'bird', 'cat', 'dog', 'elephant', 'dog'], 
# the distance between the first and second occurrences of 'dog' is 4 and 
# the distance between the second and third occurrences of 'dog' is 2. 
# Therefore, the shortest distance for 'dog' should be considered 2.

def solution(word_list):
    last_occurence = {}
    min_distance = {}
    for i, word in enumerate(word_list):
        if word in min_distance:
            min_distance[word] = min(min_distance[word], i - last_occurence[word])
        else:
            min_distance[word] = float('inf')
        last_occurence[word] = i
    
    delete_items = []
    for key, val in min_distance.items():
        if val == float('inf'):
            delete_items.append(key)

    for k in delete_items:
        del min_distance[k]
    
    return min_distance


