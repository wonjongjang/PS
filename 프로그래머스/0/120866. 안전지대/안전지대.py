def solution(board):
    n = len(board)
    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]
    
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                for d in range(8):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                        board[nx][ny] = 2
                        
    answer = 0
    
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                answer += 1
    
    return answer



# def solution(board):
#     n = len(board)
#     danger_zone = set()
    
#     # 1. 보드 전체를 순회하며 지뢰(1)의 위치를 찾습니다.
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] == 1:
#                 # 2. 지뢰를 발견하면, 자기 자신을 포함한 9방향의 좌표를 계산합니다.
#                 for dx in [-1, 0, 1]:
#                     for dy in [-1, 0, 1]:
#                         nx, ny = i + dx, j + dy
                        
#                         # 3. 계산된 좌표가 보드 판(N x N) 안에 존재하는지(유효한지) 검사합니다.
#                         if 0 <= nx < n and 0 <= ny < n:
#                             danger_zone.add((nx, ny))
                            
#     # 4. 전체 칸 수(n * n)에서 위험 지역으로 판별된 칸의 수를 빼서 안전지대를 구합니다.
#     return n * n - len(danger_zone)