def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i] + str2[i]
    
    return answer

# def solution(str1, str2):
#     return ''.join(a + b for a, b in zip(str1, str2))