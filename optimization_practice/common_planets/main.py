# Indicate whether a celestial body from List1 is found in List2
# This time we have to use a loop to iterate over the list1, cause the result array
# should indicate the status of each celestial/planet, so we use set for list2 only

def solution(list1, list2):
    # TODO: implement the solution and return the result list.
    list2 = set(list2)
    result = []
    for item in list1:
        if item in list2:
            result.append(True)
        else:
            result.append(False)
    # or we can write a shortcut like this
    # result = [item in list2 for item in list1]
    return result