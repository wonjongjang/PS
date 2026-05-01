def solution(arr):
    rows = len(arr)
    cols = len(arr[0])
    
    if rows == cols:
        return arr
    
    n = max(rows, cols)
    answer = [[0] * n for _ in range(n)]
    
    for i in range(rows):
        for j in range(cols):
            answer[i][j] = arr[i][j]
            
    return answer



# def solution(arr):
#     rows = len(arr)
#     cols = len(arr[0])

#     if rows > cols:
#         for row in arr:
#             row.extend([0] * (rows - cols))
#     elif cols > rows:
#         for _ in range(cols - rows):
#             arr.append([0] * cols)

#     return arr