from collections import Counter

def solution(my_string):
    answer = [0] * 52
    
    for ch in my_string:
        if 'A' <= ch <= 'Z':
            answer[ord(ch) - ord('A')] += 1
        else:
            answer[ord(ch) - ord('a') + 26] += 1
    
    return answer