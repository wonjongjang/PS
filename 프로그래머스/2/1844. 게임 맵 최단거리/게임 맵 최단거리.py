def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    visited = list([0] * m for _ in range(n))
    answer = -1
    
    def bfs(i, j):
        nonlocal answer
        
        visited[i][j] = 1
        queue = [(i, j)]
        
        while queue:
            x, y = queue.pop(0)
            
            if x == n-1 and y == m-1:
                answer = visited[x][y]
                break
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    
    bfs(0, 0)
    
    return answer

# 시간복잡도: O(n*m)
# from collections import deque

# def solution(maps):
#     n = len(maps)
#     m = len(maps[0])

#     # 상, 하, 좌, 우
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     queue = deque()
#     queue.append((0, 0))

#     while queue:
#         x, y = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             # 맵 안에 있고, 길(1)인 경우만 이동
#             if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
#                 maps[nx][ny] = maps[x][y] + 1
#                 queue.append((nx, ny))

#     # 도착점에 도달하지 못한 경우
#     if maps[n - 1][m - 1] == 1: