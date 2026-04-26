def solution(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)
    
    if len1 == len2:
        diff = sum(arr1) - sum(arr2)
        if diff > 0:
            return 1
        elif diff == 0:
            return 0
        else:   # diff < 0
            return -1
    else:
        return 1 if len1 > len2 else -1