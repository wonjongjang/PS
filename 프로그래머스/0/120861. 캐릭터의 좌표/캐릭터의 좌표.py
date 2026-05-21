def solution(keyinput, board):
    d = {
        "up": (0, 1),
        "down": (0, -1),
        "left": (-1, 0),
        "right": (1, 0)
    }
    
    answer = [0, 0]
    limit = [board[0] // 2, board[1] // 2]
    
    for key in keyinput:
        temp = d[key]
        if abs(answer[0] + temp[0]) <= abs(limit[0]) and abs(answer[1] + temp[1]) <= abs(limit[1]):
            answer[0] += temp[0]
            answer[1] += temp[1]
            
    return answer



# def solution(keyinput, board):
#     # 1. 각 방향키에 따른 x, y 이동 변화량을 딕셔너리로 정의합니다.
#     moves = {
#         "up": (0, 1),
#         "down": (0, -1),
#         "left": (-1, 0),
#         "right": (1, 0)
#     }
    
#     # 2. 현재 좌표와 맵의 최대 이동 가능 범위(절댓값)를 구합니다.
#     x, y = 0, 0
#     limit_x = board[0] // 2
#     limit_y = board[1] // 2
    
#     # 3. 입력된 방향키를 순회하며 이동을 시도합니다.
#     for key in keyinput:
#         dx, dy = moves[key]
#         nx, ny = x + dx, y + dy
        
#         # 4. 이동하려는 좌표가 맵의 경계선 안쪽일 때만 실제 좌표를 갱신합니다.
#         if -limit_x <= nx <= limit_x and -limit_y <= ny <= limit_y:
#             x, y = nx, ny
            
#     return [x, y]