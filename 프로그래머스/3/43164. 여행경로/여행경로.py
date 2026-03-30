def solution(tickets):
    answer = ['ICN']
    visited = [False] * len(tickets)
    tickets.sort()
    
    def dfs(x, n):
        if n == len(tickets):
            return True
        
        for i, (departure, arrival) in enumerate(tickets):
            if departure == x and not visited[i]:
                visited[i] = True
                answer.append(arrival)
                
                if dfs(arrival, n+1):
                    return True
                
                answer.pop()
                visited[i] = False
                
    dfs('ICN', 0)
    return answer