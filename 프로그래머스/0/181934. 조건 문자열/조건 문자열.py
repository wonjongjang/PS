def solution(ineq, eq, n, m):
    temp = ineq + eq
    
    if temp == ">=":
        return 1 if n >= m else 0
    elif temp == "<=":
        return 1 if n <= m else 0
    elif temp == ">!":
        return 1 if n > m else 0
    else:   # "<!"
        return 1 if n < m else 0