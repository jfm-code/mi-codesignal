# Your function must extract the sender's email address and count the number of emails received from each sender, 
# outputting a list of tuples.
# The tuples should be sorted by the descending order of these counts. If two senders have sent the same number of 
# emails, the tuples should be listed in ascending order based on the senders' email addresses.

def organize_inbox(inbox_string):
    inbox_list = inbox_string.split(';')
    dict = {}
    for inbox in inbox_list:
        objects = inbox.split(", ")
        email = objects[0].strip() #strip() to prevent the trailing spaces
        dict[email] = dict.get(email, 0) + 1
    
    result = dict.items() # convert to a list first to use sorted() function
    result = sorted(result, key=lambda x: (-x[1], x[0])) 
    # x is each key-value object, we sort it -x[1] means sorting descending values first (values is counts here) 
    # then x[0] means sorting ascending keys (keys is emails here)
    return result

organize_inbox("JohnDoe@gmail.com, Subject1, 09:00; JaneDoe@gmail.com, Subject2, 10:00; JohnDoe@gmail.com, Subject3, 12:00; Bot@gmail.com, Subject4, 08:00; Bot@gmail.com, Subject5, 09:00")