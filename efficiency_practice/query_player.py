def query_player(player_ids, player_scores, queries):
    hashmap = {}
    for id, score in zip(player_ids, player_scores):
        if id not in hashmap:
            hashmap[id] = score

    result = []
    for id in queries:
        if id in hashmap:
            result.append(hashmap[id])
    return result

ids = [1, 2, 3, 4, 5]
scores = [100, 200, 150, 50, 300]
q = [2, 5, 1] # find the score of player with ID 2, 5 and 1
print(query_player(ids, scores, q))
# Expected output: [200, 300, 100]