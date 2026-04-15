def solution(my_strings, parts):
    answer = ''
    
    for string, (s, e) in zip(my_strings, parts):
        answer += string[s:e+1]
    
    return answer

# def solution(my_strings, parts):
#     return ''.join(s[a:b+1] for s, (a, b) in zip(my_strings, parts))