def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        answer.append(min([x for x in arr[s:e+1] if x > k], default=-1))
        
    return answer