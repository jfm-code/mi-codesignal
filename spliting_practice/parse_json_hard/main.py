# This time, we return the updated list of dictionaries, not just a dictionary/hashmap
# The hardest test case is test case 5, where the value to be updated is a nested json -> we need to parse that first
# To handle test case 5, we should parse the new_value json first into a map, then when we hit the keys, replace that values with new values in the new_value map.

def parse_sub_json(data, changekey, changevalue, ischange):
    if ',' in data:
        obj_list = data.split(',')
    else:
        obj_list = data.split(';')
    hashmap = {}
    for obj in obj_list:
        key, val = obj.split('=', 1)
        if '(' not in val:
            if key == changekey and ischange == True and '{' not in changevalue:
                hashmap[key] = changevalue
            elif key in changevalue and ischange == True: # handle the case where the changevalue is a json
                hashmap[key] = changevalue[key]
            else:
                hashmap[key] = val
        else:
            hashmap[key] = parse_sub_json(val[1:-1], changekey, changevalue, ischange)
    return hashmap

def solution(data, userid, userkey, new_value):
    # if the new_value is a nested json, turn that into a map first
    if '(' in new_value:
        new_value = parse_sub_json(new_value[1:-1], '', '', False)
    # otherwise, use the given new_value
    data = data.split('\n')
    map_list = []
    for user in data:
        user_map = {}
        key, val = user.split(',', 1)
        if ',' not in val:
            user_map[key] = val
        else:
            if key != userid:
                modify = False
            else:
                modify = True
            user_map[key] = parse_sub_json(val, userkey, new_value, modify)
        map_list.append(user_map)

    return map_list

# test case 5 (the hardest test case)
sample_input = '001,Name=John,Address=(Street=Main St;City=NY;Zip=10001),Email=john@gmail.com\n002,Name=Jane,Address=(Street=2nd St;City=LA;Zip=90001),Email=jane@hotmail.com'
userID = '002'
update_key = 'Address'
new_val = '(Street=3rd Ave;City=SF;Zip=94101)'
sample_output = [
    {
        '001': {
            'Name': 'John', 
            'Address': {
                'Street': 'Main St', 
                'City': 'NY', 
                'Zip': '10001'
            }, 
            'Email': 'john@gmail.com'
        }
    }, 
    {
        '002': {
            'Name': 'Jane', 
            'Address': {
                'Street': '3rd Ave', 
                'City': 'SF', 
                'Zip': '94101'
            }, 
            'Email': 'jane@hotmail.com'
        }
    }
]

print(solution(sample_input, userID, update_key, new_val))