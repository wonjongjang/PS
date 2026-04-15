def solution(intStrs, k, s, l):
    answer = []
    for intStr in intStrs:
        temp = int(intStr[s:s+l])
        if temp > k:
            answer.append(temp)
    
    return answer

# def solution(intStrs, k, s, l):
#     return [num for x in intStrs if (num := int(x[s:s+l])) > k]