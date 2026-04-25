def solution(arr, k):
    answer = []
    check = set()
    
    for n in arr:
        if len(answer) == k:
            return answer
            
        if n not in check:
            check.add(n)
            answer.append(n)
    
    return answer + [-1] * (k - len(answer))