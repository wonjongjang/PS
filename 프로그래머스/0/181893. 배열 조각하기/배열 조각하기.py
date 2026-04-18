def solution(arr, query):
    for i, q in enumerate(query):
        if i % 2:   # 홀수
            arr = arr[q:]
        else:   # 짝수
            arr = arr[:q+1]
    return arr

# def solution(arr, query):
#     left = 0
#     right = len(arr) - 1

#     for i, q in enumerate(query):
#         if i % 2 == 0:
#             right = left + q
#         else:
#             left = left + q

#     return arr[left:right + 1]