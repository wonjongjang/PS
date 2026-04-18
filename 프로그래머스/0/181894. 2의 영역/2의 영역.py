def solution(arr):
    temp = []
    for i, n in enumerate(arr):
        if n == 2:
            temp.append(i)
    
    if temp:
        return arr[temp[0]:temp[-1]+1]
    else:
        return [-1]
    
# def solution(arr):
#     if 2 not in arr:
#         return [-1]
    
#     start = arr.index(2)
#     end = len(arr) - 1 - arr[::-1].index(2)
    
#     return arr[start:end+1]