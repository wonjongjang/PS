def solution(a, b):
    if a % 2 and b % 2: # 모두 홀수라면
        return a ** 2 + b ** 2
    elif not a % 2 and not b % 2:   # 모두 홀수가 아니라면
        return abs(a - b)
    else:   # 하나만 홀수라면
        return 2 * (a + b)