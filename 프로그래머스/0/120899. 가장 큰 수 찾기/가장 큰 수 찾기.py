def solution(array):
    max_val = max(array)
    max_idx = array.index(max_val)
    
    return [max_val, max_idx]