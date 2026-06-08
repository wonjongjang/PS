def solution(common):
    a, b, c = common[0], common[1], common[2]
    
    if b - a == c - b:
        return common[-1] + (b - a)
    else:
        return common[-1] * (b // a)