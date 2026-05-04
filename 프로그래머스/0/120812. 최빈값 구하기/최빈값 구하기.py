from collections import Counter

def solution(array):
    most_common = Counter(array).most_common()
    
    # 최빈값이 여러 개
    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        return -1
    
    return most_common[0][0]