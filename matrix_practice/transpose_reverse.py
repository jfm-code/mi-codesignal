

# Function to transpose the seating chart (Matrix) for new arrangement
def transpose(chart):
    rows = len(chart)
    cols = len(chart[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = chart[i][j]
    
    reverse_result = []
    for arr in result[::-1]: # reverse matrix
        reverse_result.append(arr)
    return reverse_result

# Given a constant matrix that represents tables in a restaurant
seating_chart = [
    [101, 102, 103, 104],
    [201, 202, 203, 204],
    [301, 302, 303, 304]
]

transposed_seating = transpose(seating_chart)
print(transposed_seating)
# The expected output - [[104, 204, 304], [103, 203, 303], [102, 202, 302], [101, 201, 301]]