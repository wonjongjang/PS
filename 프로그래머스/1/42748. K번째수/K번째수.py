def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
    
    return answer
    
   





        
    # return answer

# def solution(array, commands):
#     answer = []
    
#     for command in commands:
#         i, j, k = command
        
#         slice = array[i-1:j]        # 자르기 (array 0번 요소를 1번으로 적용하기 위해 i-1)
#         slice.sort()                # 정렬
        
#         answer.append(slice[k-1])   # k번째 숫자 (0번 요소를 1번으로 적용하기 위해 k-1)
        
#     return answer