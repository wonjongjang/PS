def solution(citations):
    temp = sorted(citations, reverse=True)

    answer = 0
    for i, t in enumerate(temp):
        if t >= i + 1:
            answer = i + 1
        else:
            break    
    
    return answer

# 1
# def solution(citations):
#     citations.sort(reverse=True)

#     for i, citation in enumerate(citations, start=1):
#         if citation < i:
#             return i - 1

#     return len(citations)