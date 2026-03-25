from collections import Counter # 문자열 개수, 숫자 개수, 동명이인 처리

def solution(participant, completion):
    count = Counter(participant) - Counter(completion)
    
    return list(count.keys())[0] # dict_keys 형태를 list 형태로 변환 (인덱스 접근 수월 위해)