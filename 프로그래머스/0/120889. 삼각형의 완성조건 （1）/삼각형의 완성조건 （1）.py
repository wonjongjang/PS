def solution(sides):
    a, b, c = sorted(sides)
    return 1 if a + b > c else 2