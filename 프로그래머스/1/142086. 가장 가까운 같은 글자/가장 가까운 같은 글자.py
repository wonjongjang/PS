def solution(s):
    answer = []
    hsh = {}
    for i, ch in enumerate(s):
        if ch in hsh:
            answer.append(i - hsh[ch])
            hsh[ch] = i
        else:
            answer.append(-1)
            hsh[ch] = i
        
    return answer

# def solution(s):
#     last = {}
#     answer = []
    
#     for i, ch in enumerate(s):
#         if ch in last:
#             answer.append(i - last[ch])
#         else:
#             answer.append(-1)
        
#         last[ch] = i
    
#     return answer