def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    
    def recur(x):
        visited[x] = 1
        
        for j in range(n):
            if visited[j] == 0 and computers[x][j]:
                recur(j)

    for i in range(n):
        if not visited[i]:
            answer += 1
            recur(i)
            
    return answer

# def solution(n, computers):
#     visited = [False] * n

#     def dfs(x):
#         visited[x] = True

#         for y in range(n):
#             if computers[x][y] == 1 and not visited[y]:
#                 dfs(y)

#     answer = 0

#     for i in range(n):
#         if not visited[i]:
#             dfs(i)
#             answer += 1

#     return answer