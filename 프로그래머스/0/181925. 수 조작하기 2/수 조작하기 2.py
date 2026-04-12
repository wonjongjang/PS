def solution(numLog):
    answer = []
    
    for i in range(1, len(numLog)):
        temp = numLog[i] - numLog[i - 1]
        
        if temp == 1:
            answer.append('w')
        elif temp == -1:
            answer.append('s')
        elif temp == 10:
            answer.append('d')
        else:   # temp == -10
            answer.append('a')
    
    return ''.join(answer)

# def solution(numLog):
#     cmd = {
#         1: 'w',
#         -1: 's',
#         10: 'd',
#         -10: 'a'
#     }
    
#     answer = []
    
#     for i in range(1, len(numLog)):
#         diff = numLog[i] - numLog[i - 1]
#         answer.append(cmd[diff])
    
#     return ''.join(answer)