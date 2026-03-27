def solution(numbers):
    temp = list(map(str, numbers))
    temp.sort(key=lambda x: x * 3, reverse=True)
    
    return str(int(''.join(temp)))

# 1
# from functools import cmp_to_key

# def compare(a, b):
#     if a + b > b + a:
#         return -1
#     elif a + b < b + a:
#         return 1
#     else:
#         return 0

# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=cmp_to_key(compare))
#     return str(int("".join(numbers)))