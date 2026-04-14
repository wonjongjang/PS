from collections import Counter

def solution(a, b, c, d):
    counter = Counter([a, b, c, d])
    length = len(counter)
    
    if length == 1: # 숫자가 모두 같을 때
        return 1111 * a
    
    elif length == 2:
        p, q = counter.most_common()
        if p[1] == 3:
            return (10 * p[0] + q[0]) ** 2
        else:
            return (p[0] + q[0]) * (abs(p[0] - q[0]))
        
    elif length == 3:
        temp = 1
        for k, v in counter.items():
            if v == 1:
                temp *= k
        return temp
    
    else:   # 숫자가 모두 다를 때
        return min(a, b, c, d)
    
    
# from collections import Counter

# def solution(a, b, c, d):
#     counter = Counter([a, b, c, d])
#     kinds = len(counter)

#     if kinds == 1:
#         return 1111 * a

#     elif kinds == 2:
#         (p, p_cnt), (q, q_cnt) = counter.most_common()

#         if p_cnt == 3:
#             return (10 * p + q) ** 2
#         else:
#             return (p + q) * abs(p - q)

#     elif kinds == 3:
#         singles = [num for num, cnt in counter.items() if cnt == 1]
#         return singles[0] * singles[1]

#     else:
#         return min(a, b, c, d)