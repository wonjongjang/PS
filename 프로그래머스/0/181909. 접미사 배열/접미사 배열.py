def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i:])
    
    answer.sort()
    return answer

# def solution(my_string):
#     return sorted(my_string[i:] for i in range(len(my_string)))