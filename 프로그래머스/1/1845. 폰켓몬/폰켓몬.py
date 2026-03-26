# from collections import Counter

def solution(nums):
    # count = Counter(nums)
    # print(count)
    
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1
    
    return min(len(count), len(nums)//2)
    
# def solution(nums):
#     return min(len(set(nums)), len(nums)//2)