def solution(num_list):
    sum_v = 0
    mul_v = 1
    
    for n in num_list:
        sum_v += n
        mul_v *= n
    
    return 1 if (sum_v ** 2) > mul_v else 0