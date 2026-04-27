def solution(rank, attendance):
    a, b, c = sorted([(r, i) for i, (r, a) in enumerate(zip(rank, attendance)) if a])[:3]
    
    return 10000 * a[1] + 100 * b[1] + c[1]