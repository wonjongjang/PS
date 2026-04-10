from collections import Counter

def solution(str1, str2):
    A = []
    B = []
    for i in range(len(str1)-1):
        temp = str1[i] + str1[i+1]
        if temp.isalpha():
            A.append(temp.upper())
    for i in range(len(str2)-1):
        temp = str2[i] + str2[i+1]
        if temp.isalpha():
            B.append(temp.upper())
    
    if not A and not B: # 집합 A와 집합 B가 모두 공집합일 경우
        return 65536
    
    answer = 1  # 자카드 유사도 J(A, B)
    count_A = Counter(A)
    count_B = Counter(B)
    
    inter = count_A & count_B
    union = count_A | count_B
    answer = sum(inter.values()) / sum(union.values())
    
    return int(answer * 65536)


# from collections import Counter

# def solution(str1, str2):
#     def make(s):
#         result = []
#         for i in range(len(s) - 1):
#             a, b = s[i], s[i+1]
#             if a.isalpha() and b.isalpha():
#                 result.append((a + b).lower())
#         return result
    
#     s1 = Counter(make(str1))
#     s2 = Counter(make(str2))
    
#     # 교집합
#     inter = sum((s1 & s2).values())
#     # 합집합
#     union = sum((s1 | s2).values())
    
#     if union == 0:
#         return 65536
    
#     return int((inter / union) * 65536)