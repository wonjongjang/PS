def solution(hp):
    answer = 0
    
    for power in [5, 3, 1]:
        answer += hp // power
        hp %= power
    
    return answer



# def solution(hp):
#     return hp // 5 + (hp % 5) // 3 + (hp % 5) % 3