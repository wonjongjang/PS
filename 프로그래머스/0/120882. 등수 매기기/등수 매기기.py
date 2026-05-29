def solution(score):
    answer = [0] * len(score)
    temp = sorted(((sum(s) / 2, i) for i, s in enumerate(score)), reverse=True)
    
    prev = [0, 0]
    for i, (avg, idx) in enumerate(temp):
        if prev[0] == avg:
            answer[idx] = prev[1]
            continue
            
        answer[idx] = i + 1
        prev[0] = avg
        prev[1] = i + 1
    
    return answer



# def solution(score):
#     # 1. 평균을 구하는 대신 '점수의 합'을 구해 내림차순(큰 수부터) 정렬합니다.
#     # (나눗셈을 하지 않아 소수점 오차를 원천 차단합니다)
#     sorted_sums = sorted([sum(s) for s in score], reverse=True)
    
#     # 2. 원본 점수 합이 정렬된 리스트에서 '처음으로 등장하는 인덱스'를 찾아 등수를 매깁니다.
#     return [sorted_sums.index(sum(s)) + 1 for s in score]

