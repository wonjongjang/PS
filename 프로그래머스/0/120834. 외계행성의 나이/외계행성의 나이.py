def solution(age):
    answer = []
    
    for num in str(age):
        answer.append(chr(int(num) + 97))    
    
    return ''.join(answer)



# def solution(age):
#     return ''.join(chr(int(num) + ord('a')) for num in str(age))