def solution(my_string):
    answer = 0
    temp = ''
    for s in my_string:
        if s.isdigit(): # 숫자일 때
            temp += s
        else:   # 알파벳일 때
            if temp:
                answer += int(temp)  
                temp = ''
            
    if temp:
        answer += int(temp)
        
    return answer



# import re

# def solution(my_string):
#     # 정규표현식을 이용해 문자열에서 연속된 숫자들만 모두 추출한 뒤, 정수로 변환하여 더합니다.
#     return sum(int(n) for n in re.findall(r'\d+', my_string))