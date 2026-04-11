def solution(num_list):
    odd = ''
    even = ''
    
    for n in num_list:
        if n % 2:   # 홀수
            odd += str(n)
        else:   # 짝수
            even += str(n)
            
    return int(odd) + int(even)

# def solution(num_list):
#     odd = ''.join(str(n) for n in num_list if n % 2)
#     even = ''.join(str(n) for n in num_list if n % 2 == 0)
    
#     return int(odd) + int(even)