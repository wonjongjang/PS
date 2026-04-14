def solution(my_string, queries):
    for s, e in queries:
        my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]

    return my_string

# def solution(my_string, queries):
#     arr = list(my_string)

#     for s, e in queries:
#         arr[s:e + 1] = arr[s:e + 1][::-1]

#     return ''.join(arr)