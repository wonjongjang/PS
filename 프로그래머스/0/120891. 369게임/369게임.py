def solution(order):
    answer = 0
    
    for num in str(order):
        if num in '369':
            answer += 1
            
    return answer



# def solution(order):
#     return sum(1 for char in str(order) if char in '369')