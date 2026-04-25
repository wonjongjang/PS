def solution(arr):
    answer = []
    
    for n in arr:
        answer += [n] * n
        
    return answer



# def solution(arr):
#     answer = []
    
#     for x in arr:
#         answer.extend([x] * x)
    
#     return answer