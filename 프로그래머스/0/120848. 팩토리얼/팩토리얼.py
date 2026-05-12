
def solution(n):
    factorial = 1
    i = 1
    
    while factorial <= n:
        i += 1
        factorial *= i
        
    return i - 1