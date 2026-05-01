def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    x, y = 0, 0
    d = 0
    answer[x][y] = 1
    
    while True:
        if answer[x][y] == n ** 2:
            break
        
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and not answer[nx][ny]:
            answer[nx][ny] = answer[x][y] + 1
            x, y = nx, ny
        else:
            d = (d + 1) % 4
        
    return answer



# def solution(n):
#     answer = [[0] * n for _ in range(n)]

#     x, y = 0, 0
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
#     direction = 0

#     for num in range(1, n * n + 1):
#         answer[x][y] = num

#         nx = x + dx[direction]
#         ny = y + dy[direction]

#         if not (0 <= nx < n and 0 <= ny < n) or answer[nx][ny] != 0:
#             direction = (direction + 1) % 4
#             nx = x + dx[direction]
#             ny = y + dy[direction]

#         x, y = nx, ny

#     return answer