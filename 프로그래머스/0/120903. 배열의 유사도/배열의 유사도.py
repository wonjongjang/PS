def solution(s1, s2):
    return sum(1 for x in s1 if x in s2)



# def solution(s1, s2):
#     # 두 리스트를 집합(set)으로 변환한 뒤, 교집합(&)을 구하고 그 길이를 반환
#     return len(set(s1) & set(s2))