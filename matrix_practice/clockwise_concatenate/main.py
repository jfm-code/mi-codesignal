# TODO: implement the function that extracts 'n' boundary layers from matrix_A and matrix_B,
# merges them into a single array and then returns this new array.
# I can implement this by traverse clockwise, but slicing method is simpler a bit
# For the slicing method, just be careful with the boundary indexes
# extend() function will iterate the list and append each element in that list

def extract_layer(matrix, layer):
    n = len(matrix) # num of rows = num of cols
    layer_list = []
    
    # edge case, if matrix is 1x1 then only return that top element
    if len(matrix[layer][layer:n-layer]) == 1:
        return matrix[layer][layer:n-layer]
    
     # extract top row
    layer_list.extend(matrix[layer][layer:n-layer])
    
    # extract last col
    for row in matrix[layer+1:n-layer-1]:
        layer_list.append(row[n-layer-1])
    
    # extract bottom row
    layer_list.extend(matrix[n-layer-1][layer:n-layer][::-1]) # reverse list with ::-1
    
    # extract first col
    for col in matrix[layer+1:n-layer-1][::-1]:
        layer_list.append(col[layer])
    
    return layer_list

def solution(matrix_A, matrix_B, n):
    result = []
    for i in range(n):
        result.extend(extract_layer(matrix_A, i))
    for i in range(n):
        result.extend(extract_layer(matrix_B, i))
    return result
