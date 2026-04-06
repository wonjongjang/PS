from collections import deque

def solution(n, edge):
    abj = [[] for _ in range(n + 1)]
    
    for a, b in edge:
        abj[a].append(b)
        abj[b].append(a)
    
    visited = [-1] * (n + 1)
    visited[1] = 0
    
    q = deque([1])   
    while q:
        cur = q.popleft()
        
        for nxt in abj[cur]:
            if visited[nxt] == -1:
                q.append(nxt)
                visited[nxt] = visited[cur] + 1
    
    max_v = max(visited)
    return visited.count(max_v)