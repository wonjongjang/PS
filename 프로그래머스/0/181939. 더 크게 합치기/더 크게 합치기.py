def solution(a, b):
    a, b = str(a), str(b)
    return max(int(a + b), int(b + a))