def solution(lines):
    table = [0] * 200
    
    for a, b in lines:
        for i in range(a, b):
            table[i + 100] += 1
    
    return sum(1 for x in table if x >= 2)



# def solution(lines):
#     # 1. 각 선분이 차지하는 1단위 구간을 집합(set)으로 변환합니다.
#     sets = [set(range(start, end)) for start, end in lines]
    
#     # 2. 3개의 선분 중 2개 이상 겹치는 모든 구간을 교집합(&)과 합집합(|)으로 구합니다.
#     overlap = (sets[0] & sets[1]) | (sets[1] & sets[2]) | (sets[0] & sets[2])
    
#     # 3. 최종적으로 겹치는 구간의 개수(길이)를 반환합니다.
#     return len(overlap)