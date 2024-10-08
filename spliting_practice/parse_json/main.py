# The goal is to parse the string input into a hashmap
# First of all, differentiate the outer key-pairs and inner key-pairs by using ;
# Then check if the value in key-pair has a sub JSON that need to be parse, call function recursively then


def solution(json_string, update_value):
    # Get rid of unecessary characters
    json_string = json_string.replace('\\','')
    json_string = json_string.replace('"','')
    json_string = json_string.replace(' ','')
    json_string = json_string[1:-1]

    # Replace commas , outside brackets {} with ;
    balance = 0
    new_str = ''
    for char in json_string:
        if char == '{':
            balance += 1
        elif char == '}':
            balance -= 1
        elif char == ',' and balance == 0:
            new_str += ';'
            continue # if the char is comma, replace it with ; and do not execute next line
        new_str += char
        
    # Split the stirngs
    str_list = new_str.split(';')
    
    # Push to map
    hashmap = {}
    for sub_str in str_list:
        # split 1 time only, by default it will be split the whole string
        key, value = sub_str.split(':', 1) 
        if (key not in hashmap) and ('{' not in value):
            # update value for key4 only
            if key == 'key4':
                hashmap[key] = update_value
            else:
                hashmap[key] = value
            
        # if theres a nested json, call the solution function recursively
        if '{' in value:
            hashmap[key] = solution(value, update_value)
            
    return hashmap