# This function will take as input a string of logs and output a list of tuples representing the books with the longest borrowed duration.
# If a book has been borrowed and returned multiple times, the borrowed duration is the total cumulative sum of those durations.
# If multiple books share the same longest borrowed duration, the function should return all such books in ascending order of their IDs.
from datetime import datetime

def solution(logs):
    log_list = logs.split(', ')
    hashmap = {}
    
    # Calculate the borrow time of each log
    for log in log_list:
        record = log.split(' ')
        
        if record[0] in hashmap:
            data = hashmap[record[0]]
        else:
            data = {}
        
        if record[1] == "borrow":
            data["start_t"] = datetime.strptime(record[2], "%H:%M")
        else:
            data["borrow_t"] = data.get("borrow_t", datetime.strptime("00:00", "%H:%M")) + (datetime.strptime(record[2], "%H:%M") - hashmap[record[0]]["start_t"])
        
        hashmap[record[0]] = data
    
    # Find the longest borrowing time
    max_t = datetime.strptime('00:00', "%H:%M")
    for value in hashmap.values():
        if value["borrow_t"] > max_t:
            max_t = value["borrow_t"]
    
    # Append the logs that have longest borrowing time, do not need to sort anymore cause the map already sort the keys
    result = []
    for key, value in hashmap.items():
        if value["borrow_t"] == max_t:
            tuple_data = (int(key), str(value["borrow_t"].hour).zfill(2) + ':' + str(value["borrow_t"].minute).zfill(2))
            result.append(tuple_data)
    
    return result