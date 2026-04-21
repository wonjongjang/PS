def solution(num_list):
    # 리스트의 길이가 11 이상이면
    if len(num_list) >= 11:
        return sum(num_list)
    
    # 리스트의 길이가 10 이하이면
    answer = 1
    for num in num_list:
        answer *= num
    return answer



# from math import prod

# def solution(num_list):
#     return sum(num_list) if len(num_list) >= 11 else prod(num_list)