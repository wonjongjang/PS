def solution(n):
    answer = []
    
    for i in range(1, n + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count >= 3:
            answer.append(i)
            
    return len(answer)



# def solution(n):
#     answer = 0

#     for num in range(4, n + 1):
#         for divisor in range(2, int(num ** 0.5) + 1):
#             if num % divisor == 0:
#                 answer += 1
#                 break

#     return answer