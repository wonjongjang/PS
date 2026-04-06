def solution(n, results):
    abj = [[0] * (n+1) for _ in range(n+1)]
    
    for a, b in results:
        abj[a][b] = 1
        abj[b][a] = -1
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if abj[i][j] == 1 and abj[j][k] == 1:
                    abj[i][k] = 1
                    abj[k][i] = -1
                elif abj[i][j] == -1 and abj[j][k] == -1:
                    abj[i][k] = -1
                    abj[k][i] = 1
    
    answer = 0  # 정확하게 순위를 매길 수 있는 선수의 수
    
    for i in range(1, n+1):
        count = 0
        for j in range(1, n+1):
            if i != j and abj[i][j] != 0:
                count += 1
                
        if count == n-1:
            answer += 1
    
    return answer