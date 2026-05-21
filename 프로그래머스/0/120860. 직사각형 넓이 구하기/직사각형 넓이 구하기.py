def solution(dots):
    a, b, c, d = sorted(dots)
    return (c[0] - a[0]) * (b[1] - a[1])