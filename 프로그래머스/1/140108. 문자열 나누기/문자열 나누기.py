def solution(s):
    answer = 0
    count_x = 0
    count_oth = 0
    x = s[0]
    
    for i in s:
        if count_x == 0:
            x = i
        
        if x == i:
            count_x += 1
        else:
            count_oth += 1
            
        if count_x == count_oth:
            answer += 1
            count_x = 0
            count_oth = 0
    
    if count_x != 0:
        answer += 1
    
    return answer