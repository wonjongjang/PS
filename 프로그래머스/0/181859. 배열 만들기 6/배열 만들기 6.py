def solution(arr):
    stk = []
    i = 0
    
    while i < len(arr):
        if stk:
            if stk[-1] == arr[i]:
                stk.pop()
            else:
                stk.append(arr[i])
        else:
            stk.append(arr[i])
        
        i += 1
    
    return stk if stk else [-1]



# def solution(arr):
#     stk = []

#     for x in arr:
#         if stk and stk[-1] == x:
#             stk.pop()
#         else:
#             stk.append(x)

#     return stk if stk else [-1]