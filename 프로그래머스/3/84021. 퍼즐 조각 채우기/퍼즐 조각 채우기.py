from collections import deque

def solution(game_board, table):
    n = len(game_board)
    
    # 1. 도형 추출
    def bfs(sx, sy, board, target):
        q = deque([(sx, sy)])
        board[sx][sy] = -1
        cells = [(sx, sy)]
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        while q:
            x, y = q.popleft()
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == target:
                    board[nx][ny] = -1
                    q.append((nx, ny))
                    cells.append((nx, ny))
                    
        return cells
    
    # 2. 도형 정규화
    def normalize(cells):
        min_x = min(x for x, y in cells)
        min_y = min(y for x, y in cells)
        normalized = [(x - min_x, y - min_y) for x, y in cells]
        normalized.sort()    # 비교하기 쉽게 순서를 맞추는 용도
        return normalized
    
    # 3. 도형 회전
    def rotate(cells):
        rotated = [(y, -x) for x, y in cells]
        return normalize(rotated)
        
    blanks = []
    pieces = []
    
    for x in range(n):
        for y in range(n):
            if game_board[x][y] == 0:
                blank = bfs(x, y, game_board, 0)
                blanks.append(normalize(blank))
                
            if table[x][y] == 1:
                piece = bfs(x, y, table, 1)
                pieces.append(normalize(piece))
            
    used = [False] * len(pieces)    # 퍼즐 사용 여부
    answer = 0
    
    for blank in blanks:
        for i in range(len(pieces)):
            if used[i]:
                continue
            if len(blank) != len(pieces[i]):
                continue
                
            piece = pieces[i]
            matched = False
            
            # 4. 회전 비교
            for _ in range(4):
                if blank == piece:
                    matched = True
                    break
                piece = rotate(piece)
            
            # 매칭
            if matched:
                used[i] = True
                answer += len(blank)
                break
            
    return answer