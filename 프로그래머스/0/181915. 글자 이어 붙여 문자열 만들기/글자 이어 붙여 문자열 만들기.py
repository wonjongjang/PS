def solution(my_string, index_list):
    answer = ''
    
    for index in index_list:
        answer += my_string[index]
        
    return answer

# def solution(my_string, index_list):
#     return ''.join(my_string[i] for i in index_list)