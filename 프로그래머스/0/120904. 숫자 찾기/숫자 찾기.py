def solution(num, k):
    target = str(k)
    
    for i, n in enumerate(str(num)):
        if n == target:
            return i + 1
    
    return -1



# def solution(num, k):
#     # 문자열 앞에 임의의 문자('-')를 붙여 0으로 시작하는 인덱스를 1부터 시작하도록 만듭니다.
#     return ('-' + str(num)).find(str(k))