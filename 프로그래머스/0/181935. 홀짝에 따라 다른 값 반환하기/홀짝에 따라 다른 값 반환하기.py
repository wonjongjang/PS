def solution(n):
    answer = 0
    
    if n % 2 == 0:  # 짝수일 때
        for i in range(2, n+1, 2):
            answer += i * i # 제곱의 합
    else:   # 홀수일 때
        for i in range(1, n+1, 2):
            answer += i
        
    return answer

# def solution(n):
#     if n % 2 == 1:
#         return sum(i for i in range(1, n+1, 2))
#     else:
#         return sum(i*i for i in range(2, n+1, 2))