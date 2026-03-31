def solution(k, dungeons):
    answer = 0  # 유저가 탐험할수 있는 최대 던전 수
    visited = [False] * len(dungeons)
    
    def dfs(rem, cnt):
        nonlocal answer
        answer = max(answer, cnt)
        
#         if answer == len(dungeons):
#             return
        
#         if cnt == len(dungeons):
#             return
        
        for i, (x, y) in enumerate(dungeons):
            if rem >= x and not visited[i]:
                visited[i] = True
                dfs(rem - y, cnt + 1)
                visited[i] = False
    
    dfs(k, 0)
    
    return answer

# def solution(k, dungeons):
#     answer = 0
#     visited = [False] * len(dungeons)

#     def dfs(current_fatigue, count):
#         nonlocal answer
#         answer = max(answer, count)

#         for i in range(len(dungeons)):
#             required, consume = dungeons[i]

#             if not visited[i] and current_fatigue >= required:
#                 visited[i] = True
#                 dfs(current_fatigue - consume, count + 1)
#                 visited[i] = False

#     dfs(k, 0)
#     return answer