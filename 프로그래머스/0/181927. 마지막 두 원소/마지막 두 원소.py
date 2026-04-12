def solution(num_list):
    last = num_list[-1] # 마지막 원소
    prev = num_list[-2] # 그전 원소
    
    if last > prev:
        num_list.append(last - prev)
    else:
        num_list.append(last * 2)
        
    return num_list