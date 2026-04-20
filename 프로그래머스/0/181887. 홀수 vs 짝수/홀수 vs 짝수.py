def solution(num_list):
    odd, even = 0, 0
    
    for i, num in enumerate(num_list):
        if i % 2:
            odd += num
        else:
            even += num
        
    return max(odd, even)

# def solution(num_list):
#     odd = sum(num_list[::2])
#     even = sum(num_list[1::2])
#     return max(odd, even)