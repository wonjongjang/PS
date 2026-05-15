def solution(array, n):
    return sorted((abs(n - num), num) for num in array)[0][1]



# def solution(array, n):
#     return min(array, key=lambda x: (abs(x - n), x))