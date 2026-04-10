def solution(s):
    answer = ''
    
    idx = 0
    for ch in s:
        if ch == ' ':    # 공백
            answer += ' '
            idx = 0
            continue
            
        if idx % 2: # 홀수
            answer += ch.lower()
        else:   # 짝수
            answer += ch.upper()
        idx += 1
    
    return answer