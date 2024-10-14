# The goal is to group the substring so that all characters c belongs to only 1 group
# To do this, keep track of the last occurrences of all characters first
# Then iterate through the string, when current char matches the farthest char, end the substring
# Example: "abacbc"
    # Last occurences: a last appears at index 2, b last appears at index 4, c last appears at index 5
    # Iterate through the string:
        # Start at index 0 with a. The farthest last occurrence is 2 (for a).
        # Move to index 1 with b. The farthest last occurrence updates to 4 (for b).
        # Move to index 2 with a. The farthest last occurrence remains 4.
        # Move to index 3 with c. The farthest last occurrence updates to 5 (for c).
        # Move to index 4 with b. The farthest last occurrence remains 5.
        # Move to index 5 with c. The farthest last occurrence is 5, which matches the current position.
# So the only substring is the whole array with length 6


def string_partition(s):
    # Find the last occurrences of all characters
    last_occurence = {}
    for i, char in enumerate(s):
        last_occurence[char] = i
        
    # Iterate the string and group the substring
    end_i = 0 # end index of substring
    start_i = 0 # start index of substring
    result = []
    for i, char in enumerate(s):
        end_i = max(last_occurence[char], end_i)
        if i == end_i:
            result.append(end_i - start_i + 1)
            start_i = i + 1 # update start index when a substring ends
    return result
    
# print(string_partition("feepplkpadaasdr"))