def solution(arrows):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    
    visited_node = set()
    visited_edge = set()
    
    x, y = 0, 0
    visited_node.add((x, y))
    
    answer = 0
    
    for arrow in arrows:
        for _ in range(2):
            nx = x + dx[arrow]
            ny = y + dy[arrow]
            if (nx, ny) in visited_node and not ((x, y), (nx, ny)) in visited_edge:
                answer += 1
            
            visited_node.add((nx, ny))
            visited_edge.add(((x, y), (nx, ny)))
            visited_edge.add(((nx, ny), (x, y)))
            
            x, y = nx, ny
    
    return answer