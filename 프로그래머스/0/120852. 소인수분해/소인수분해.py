def solution(n):
    answer = []
    d = 2
    
    while d <= n:
        if n % d == 0:
            answer.append(d)
            
            while n % d == 0:
                n //= d
        else:
            d += 1
    
    return answer