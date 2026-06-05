def solution(A, B):
    list_A, list_B = list(A), list(B)
    len_A = len(A)
    
    i = 0
    while i < len_A:
        if list_A == list_B:
            return i
            
        ch = list_B.pop(0)
        list_B.append(ch)
        
        i += 1
        
    return -1



# def solution(A, B):
#     # 밀어진 결과(B)를 2번 이어 붙인 뒤, 그 안에서 원본(A)이 어디 있는지 찾습니다.
#     return (B * 2).find(A)



# from collections import deque

# def solution(A, B):
#     # 1. 두 문자열을 리스트 형태의 덱(deque)으로 변환합니다.
#     dq_A = deque(A)
#     dq_B = deque(B)
    
#     # 2. 문자열의 길이만큼 최대 회전을 시도합니다.
#     for i in range(len(A)):
#         if dq_A == dq_B:
#             return i
            
#         # 3. 우측으로 1칸 회전시킵니다. (맨 뒤의 요소가 맨 앞으로 옴)
#         dq_A.rotate(1)
        
#     # 4. 다 돌려봤는데도 일치하지 않으면 -1을 반환합니다.
#     return -1