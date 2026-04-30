def solution(picture, k):
    answer = []
    
    for p in picture:
        temp = ''.join(x * k for x in p)
        answer.extend([temp] * k)
    
    return answer