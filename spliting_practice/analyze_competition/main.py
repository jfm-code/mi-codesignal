# output a list of tuples, representing the score, successful attempts, total penalties.
# tuples should be sorted by the decreasing order of scores
# there will be no students with the same positive score
# don't include students in the output who haven't solved any problem (score=0)

def analyze_competition(logs):
    # analyze data, push into hashmap
    hashmap = {}
    log_list = logs.split(", ")
    for record in log_list:
        infos = record.split(" ")
        
        if infos[0] not in hashmap: #infos[0] = peopleID
            people_map = {} #if the user is not in map, create an empty people_map
        else:
            people_map = hashmap[infos[0]]
        
        if "success" not in people_map:
            people_map["success"] = 0
        if "fail" not in people_map:
            people_map["fail"] = 0
        if "score" not in people_map:
            people_map["score"] = 0
        
        if infos[1] == "solve":            
            people_map["score"] += int(infos[3])
            people_map["success"] += 1
        else:
            people_map["fail"] += 1
            
        hashmap[infos[0]] = people_map
        # print("DEBUG: user", infos[0], "map is", hashmap[infos[0]])
        
    #filter, extract data convert to tuple list
    result = []
    for ID, data in hashmap.items():
        if data["score"] > 0:
            result.append((int(ID), data["score"], data["success"], data["fail"]))
    
    # filter, order the list
    result = sorted(result, key=lambda obj: (-obj[1]))
    print("DEBUG:", result)
    return result