def solution(n, t):
    return n * (2 ** t)



def solution(n, t):
    # 비트 왼쪽 시프트(<<) 연산자를 사용하여 n을 2의 t승만큼 곱해줍니다.
    return n << t