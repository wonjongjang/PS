from itertools import product

def solution(l, r):
    temp = list(product(['0', '5'], repeat=len(str(r))))
    
    answer = []
    for t in temp:
        num = int(''.join(t))
        if l <= num <= r:
            answer.append(num)
    
    return answer if answer else [-1]

# def solution(l, r):
#     answer = []

#     for num in range(l, r + 1):
#         if set(str(num)) <= {'0', '5'}:
#             answer.append(num)

#     return answer if answer else [-1]