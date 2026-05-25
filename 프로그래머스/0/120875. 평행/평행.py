def solution(dots):
    [x1, y1], [x2, y2], [x3, y3], [x4, y4] = dots
    
    if (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1):
        return 1
    if (y3 - y1) * (x4 - x2) == (y4 - y2) * (x3 - x1):
        return 1
    if (y4 - y1) * (x3 - x2) == (y3 - y2) * (x4 - x1):
        return 1
    
    return 0



# def solution(dots):
#     # 두 점 사이의 기울기를 구하는 내부 함수를 정의합니다.
#     def get_slope(dot1, dot2):
#         return (dot2[1] - dot1[1]) / (dot2[0] - dot1[0])
    
#     # 4개의 점(인덱스 0, 1, 2, 3)을 두 개씩 짝짓는 3가지 모든 경우의 수를 비교합니다.
#     if get_slope(dots[0], dots[1]) == get_slope(dots[2], dots[3]):
#         return 1
#     if get_slope(dots[0], dots[2]) == get_slope(dots[1], dots[3]):
#         return 1
#     if get_slope(dots[0], dots[3]) == get_slope(dots[1], dots[2]):
#         return 1
        
#     return 0