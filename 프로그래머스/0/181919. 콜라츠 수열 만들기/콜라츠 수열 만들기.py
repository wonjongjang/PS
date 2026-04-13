def solution(n):
    answer = [n]
    
    while n != 1:
        if n % 2:   # 홀수일 때
            n = 3 * n + 1
        else:   # 짝수일 때
            n //= 2
        answer.append(n)
        
    return answer