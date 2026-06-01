def solution(chicken):
    answer = 0
    
    while chicken >= 10:
        service = chicken // 10
        leftover = chicken % 10
        
        answer += service
        
        chicken = service + leftover
    
    return answer



# def solution(chicken):
#     # 10장을 내고 1장을 돌려받으므로, 실질적으로 9장당 1마리씩 서비스받는 것과 같은 원리입니다.
#     return max(0, (chicken - 1) // 9)