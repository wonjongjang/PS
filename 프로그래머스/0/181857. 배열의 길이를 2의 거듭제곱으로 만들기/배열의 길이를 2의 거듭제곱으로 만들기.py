def solution(arr):
    temp = 1
    while temp < len(arr):
        temp *= 2
    
    return arr + [0] * (temp - len(arr))