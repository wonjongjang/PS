def solution(my_string):
    list_s = my_string.split()
    answer = int(list_s[0])
    
    for i in range(2, len(list_s), 2):
        if list_s[i - 1] == '+':
            answer += int(list_s[i])
        else:
            answer -= int(list_s[i])
        
    return answer