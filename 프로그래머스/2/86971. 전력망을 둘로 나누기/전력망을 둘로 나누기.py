from collections import deque

def solution(n, wires): 
    def bfs(start, adj, visited):
        q = deque([start])
        visited[start] = 1
        count = 1
        
        while q:
            curr = q.popleft()
            for nxt in adj[curr]:
                if not visited[nxt]:
                    visited[nxt] = 1
                    q.append(nxt)
                    count += 1
                    
        return count
    
    answer = n
    
    for cut in range(len(wires)):
        adj = [[] for _ in range(n + 1)]
        visited = [0] * (n + 1)

        # 연결
        for i, (s, e) in enumerate(wires):
            if i == cut:
                continue
            adj[s].append(e)
            adj[e].append(s)

        count = bfs(1, adj, visited)
        answer = min(answer, abs(count - (n - count)))
    
    return answer

# from collections import deque

# def solution(n, wires):
#     def bfs(start, graph, visited):
#         q = deque([start])
#         visited[start] = True
#         count = 1

#         while q:
#             now = q.popleft()
#             for nxt in graph[now]:
#                 if not visited[nxt]:
#                     visited[nxt] = True
#                     q.append(nxt)
#                     count += 1

#         return count

#     answer = n

#     for cut in range(len(wires)):
#         graph = [[] for _ in range(n + 1)]

#         for i, (a, b) in enumerate(wires):
#             if i == cut:
#                 continue
#             graph[a].append(b)
#             graph[b].append(a)

#         visited = [False] * (n + 1)
#         cnt = bfs(1, graph, visited)
#         answer = min(answer, abs(cnt - (n - cnt)))

#     return answer