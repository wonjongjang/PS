import math

def solution(progresses, speeds):
    temp = []
    for p, s in zip(progresses, speeds):
        temp.append(math.ceil((100 - p) / s))
    
    answer = []
    v = temp[0]
    count = 0
    for t in temp:
        if t <= v:
            count += 1
        else:
            answer.append(count)
            count = 1
            v = t
    
    if count:
        answer.append(count)
    
    return answer

# import math

# def solution(progresses, speeds):
#     days = [
#         math.ceil((100 - p) / s)
#         for p, s in zip(progresses, speeds)
#     ]
    
#     answer = []
#     current = days[0]
#     count = 1
    
#     for day in days[1:]:
#         if day <= current:
#             count += 1
#         else:
#             answer.append(count)
#             current = day
#             count = 1
    
#     answer.append(count)
    
#     return answer