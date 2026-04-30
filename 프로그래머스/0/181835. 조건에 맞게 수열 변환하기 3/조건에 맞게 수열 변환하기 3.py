def solution(arr, k):
    if k % 2:   # k가 홀수라면
        return [n * k for n in arr]
    else:   # k가 짝수라면
        return [n + k for n in arr]