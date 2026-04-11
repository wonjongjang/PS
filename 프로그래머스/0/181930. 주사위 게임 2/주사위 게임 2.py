def solution(a, b, c):
    s = len({a, b, c})
    
    if s == 3:
        return (a + b + c)
    elif s == 2:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    else:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
    
# def solution(a, b, c):
#     s = len({a, b, c})
    
#     sum1 = a + b + c
#     sum2 = a*a + b*b + c*c
#     sum3 = a**3 + b**3 + c**3
    
#     if s == 3:
#         return sum1
#     elif s == 2:
#         return sum1 * sum2
#     else:
#         return sum1 * sum2 * sum3