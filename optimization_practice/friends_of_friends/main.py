# Find direct friends and friends of friends
# connections = [(100, 200), (200, 300), (100, 300), (100, 400), (400, 500), (500, 600), (200, 600)]
# Person 100 connects with 200, 300, and 400. The friends of friends are 600 (from 200), 500 (from 400.Therefore, person 100 is connected to five different people within two degrees.

def find_influencer(connections):
    friends = {}
    # set up friends map with direct friends
    for tup in connections:
        if tup[0] not in friends:
            friends[tup[0]] = set()
        if tup[1] not in friends:
            friends[tup[1]] = set()
        friends[tup[0]].add(tup[1])
        friends[tup[1]].add(tup[0])
        
    # count for friends within 2 degrees (friends of friends)
    friends_of_friends = {}
    for key, val in friends.items():
        for people in val:
            if key not in friends_of_friends:
                friends_of_friends[key] = (friends[key] | friends[people]) - {key}
            else:
                friends_of_friends[key] = (friends_of_friends[key] | friends[key] | friends[people]) - {key}

    # find the candidate with highest connection but lowest value key
    max_candidate = 0
    max_connection = 0
    for candidate in friends_of_friends.keys():
        if len(friends_of_friends[candidate]) > max_connection:
            max_connection = len(friends_of_friends[candidate])
            max_candidate = candidate
        elif len(friends_of_friends[candidate]) == max_connection:
            max_candidate = min(max_candidate, candidate)
    return max_candidate