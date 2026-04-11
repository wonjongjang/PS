def solution(a, d, included):
    result = 0  # 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값
    
    for i, b in enumerate(included):
        if b:   # true일 때
            result += a + d * i
        
    return result