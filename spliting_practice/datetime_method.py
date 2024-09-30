# This function will take as input a string of logs and output a list of tuples representing the groups with 
# the longest lifetime. If multiple groups have the same longest lifetime, the function should return all such 
# groups in ascending order of their IDs.

# For example, if we have a log string as follows:
# "1 create 09:00, 2 create 10:00, 1 delete 12:00, 3 create 13:00, 2 delete 15:00, 3 delete 16:00",
# the function will return: [(2, '05:00')].

from datetime import datetime

def analyze_logs(logs):
    log_list = logs.split(", ")
    time_dict = {}
    life_dict = {}
    format = '%H:%M'

    for log in log_list:
        ID, action, time = log.split()
        ID = int(ID)
        time = datetime.strptime(time, format) # strptime() stands for string parse time

        if action == 'create':
            time_dict[ID] = time
        else: # if the act is 'delete'
            if ID in time_dict:
                life_dict[ID] = life_dict.get(ID, datetime.strptime('00:00', format)) + (time - time_dict[ID])
                del time_dict[ID]

    max_life = max(life_dict.values())  #Find the longest lifetime

    # Build the result list where each item is a tuple of group ID and its lifetime, if it has the longest lifetime.
    # If we don't convert datetime object to string, it will output the standard format like 1900-01-01 09:00:00
    # zfill() function is zeroes fill, to pad a string with zeros on the left, up to a specified width
    result = [(ID, str(life.hour).zfill(2) + ':' + str(life.minute).zfill(2)) for ID, life in
              life_dict.items() if life == max_life]

    return sorted(result)

# For PADDING, we can also use ljust() and rjust() functions:

# number = "5"
# padded_number = number.ljust(2, '0') -> if not specify the character, it will be space by default
# print(padded_number) -> Output: 50

# number = "5"
# padded_number = number.rjust(2, '0')
# print(padded_number) -> Output: 05