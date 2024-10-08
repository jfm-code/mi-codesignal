def solution(input_string, user_index, pref_key, new_value):
    # differentiate the users by replace ; with | between users and , between key-pairs in each user
    if input_string[0] == '{' and input_string[-1] == '}':
        input_string = input_string[1:-1]
    new_string = ''
    balance = 0
    for i in range(len(input_string)):
        if input_string[i] == '{':
            balance += 1
        elif input_string[i] == '}':
            balance -= 1
        elif input_string[i] == ";":
            if i < len(input_string)-4 and input_string[i+1:i+5] == "User":
                new_string += '|'
                continue
            elif balance == 0:
                new_string += ','
                continue
        new_string += input_string[i]
    
    # split string into list of users
    str_list = []
    if '|' in new_string:
        str_list = new_string.split('|')
    else:
        if ':' not in new_string:
            str_list = new_string.split(',')
        else:
            str_list.append(new_string) # edge case of 1 users only
    
    # push in the map
    hashmap = {}
    for user in str_list:
        if ':' in user:
            key, val = user.split(':')
            if key not in hashmap:
                if ',' not in val:
                    hashmap[key] = val
                else:
                    hashmap[key] = solution(val, user_index, pref_key, new_value)
        else:
            key, val = user.split('=', 1)
            if key not in hashmap:
                if '{' not in val:
                    if key == pref_key:
                        hashmap[key] = new_value
                    else:
                        hashmap[key] = val
                else:
                    hashmap[key] = solution(val, user_index, pref_key, new_value)
    
    return hashmap

# sample inputs
sample_input = "User1:Age1=21;Location1=USA;Preferences1={Food1=Italian;Sport1=Fencing};User2:Age2=30;Location2=Canada;Preferences2={Music2=Jazz;Color2=Blue}"
sample_user_index = 1
sample_pref_key = "Sport1"
sample_new_value = "Hockey"

# call function
solution(sample_input, sample_user_index, sample_pref_key, sample_new_value)

sample_output = {
  'User1': {
      'Age1': '21', 
      'Location1': 'USA', 
      'Preferences1': {
          'Food1': 'Italian',
          'Sport1': 'Hockey'
        }
    }, 
  'User2': {
      'Age2': '30', 
      'Location2': 'Canada', 
      'Preferences2': {
          'Music2': 'Jazz', 
          'Color2': 'Blue'
        }
    }
}

