def solution(num, total):
    start = (total // num) - num
    
    while True:
        temp = range(start, start + num)
        
        if sum(temp) == total:
            return list(temp)
        
        start += 1

        
        
# def solution(num, total):
#     # 1. 연속된 수들의 대략적인 '정중앙 값'을 구하고, 
#     # 그 중앙값으로부터 왼쪽으로 몇 칸을 가야 시작 숫자인지 빼줍니다.
#     start = (total // num) - ((num - 1) // 2)
    
#     # 2. 시작 숫자부터 크기가 1씩 커지는 숫자를 num개 만큼 생성합니다.
#     return [start + i for i in range(num)]