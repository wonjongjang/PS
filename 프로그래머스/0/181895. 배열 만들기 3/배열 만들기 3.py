def solution(arr, intervals):
    (a1, b1), (a2, b2) = intervals
    return arr[a1:b1+1] + arr[a2:b2+1]