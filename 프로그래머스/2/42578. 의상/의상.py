def solution(clothes):
    hash_map = {}
    
    for name, kind in clothes:
        hash_map[kind] = hash_map.get(kind, 0) + 1
    
    answer = 1
    for v in hash_map.values():
        answer *= (v + 1)   # 안 입는 경우 포함 +1
    
    return answer - 1   # 아무것도 안 입는 경우 -1

# dict에 리스트로 저장할 경우
# def group_clothes(clothes):
#     clothes_dict = {}

#     for name, kind in clothes:
#         if kind not in clothes_dict:
#             clothes_dict[kind] = []
#         clothes_dict[kind].append(name)

#     return clothes_dict