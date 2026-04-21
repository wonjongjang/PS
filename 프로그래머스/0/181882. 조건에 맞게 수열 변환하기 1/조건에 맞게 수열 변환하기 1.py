def solution(arr):
    for i, num in enumerate(arr):
        if num >= 50 and num % 2 == 0:
            arr[i] //= 2
        elif num < 50 and num % 2 == 1:
            arr[i] *= 2
    return arr



# def solution(arr):
#     answer = []

#     for x in arr:
#         if x >= 50 and x % 2 == 0:
#             answer.append(x // 2)
#         elif x < 50 and x % 2 == 1:
#             answer.append(x * 2)
#         else:
#             answer.append(x)

#     return answer