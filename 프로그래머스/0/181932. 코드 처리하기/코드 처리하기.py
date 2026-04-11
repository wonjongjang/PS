def solution(code):
    ret = ''
    mode = False    # 0
    for idx, ch in enumerate(code):
        if ch == '1':
            mode = not mode
            continue
            
        if mode:    # mode 1일 때
            if idx % 2: # 홀수
                ret += ch
        else:   # mode 0일 때
            if not idx % 2: # 짝수
                ret += ch
        
    return ret if ret else "EMPTY"


# def solution(code):
#     ret = []
#     mode = False
    
#     for idx, ch in enumerate(code):
#         if ch == '1':
#             mode = not mode
#             continue
            
#         if mode:
#             if idx % 2 == 1:
#                 ret.append(ch)
#         else:
#             if idx % 2 == 0:
#                 ret.append(ch)
        
#     return ''.join(ret) if ret else "EMPTY"

# Python에서 문자열은 immutable이라 매번 새로 생성됨 (O(n²) 가능성)
# n < 1000 정도면 괜찮음