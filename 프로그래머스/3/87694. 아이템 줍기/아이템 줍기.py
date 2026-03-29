from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    N = 102
    cp = list([0] * N for _ in range(N))
    visited = list([0] * N for _ in range(N))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for r in rectangle:
        sx, sy, ex, ey = r
        for i in range(sx*2, ex*2+1):
            for j in range(sy*2, ey*2+1):
                cp[i][j] = 1
                
    for r in rectangle:
        sx, sy, ex, ey = r
        for i in range(sx*2+1, ex*2):
            for j in range(sy*2+1, ey*2):
                cp[i][j] = 0
                
    queue = deque()
    queue.append((characterX*2, characterY*2))
    visited[characterX*2][characterY*2] = 1
    
    while queue:
        x, y = queue.popleft()
        
        if x == itemX*2 and y == itemY*2:
            return (visited[x][y] - 1) // 2
            
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and cp[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                
    return 0

# from collections import deque

# def solution(rectangle, characterX, characterY, itemX, itemY):
#     N = 102
#     board = [[0] * N for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]

#     # 1) Fill all rectangles
#     for x1, y1, x2, y2 in rectangle:
#         x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
#         for x in range(x1, x2 + 1):
#             for y in range(y1, y2 + 1):
#                 board[x][y] = 1

#     # 2) Remove inside, keep only borders
#     for x1, y1, x2, y2 in rectangle:
#         x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
#         for x in range(x1 + 1, x2):
#             for y in range(y1 + 1, y2):
#                 board[x][y] = 0

#     # 3) BFS on borders only
#     q = deque()
#     start_x, start_y = characterX * 2, characterY * 2
#     target_x, target_y = itemX * 2, itemY * 2

#     q.append((start_x, start_y))
#     visited[start_x][start_y] = 1

#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     while q:
#         x, y = q.popleft()

#         if x == target_x and y == target_y:
#             return (visited[x][y] - 1) // 2

#         for d in range(4):
#             nx = x + dx[d]
#             ny = y + dy[d]

#             if 0 <= nx < N and 0 <= ny < N:
#                 if board[nx][ny] == 1 and visited[nx][ny] == 0:
#                     visited[nx][ny] = visited[x][y] + 1
#                     q.append((nx, ny))

#     return 0