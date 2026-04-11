def solution(s):
    temp = s[2:-2].split('},{')
    s_list = [list(map(int, t.split(','))) for t in temp]
        
    s_list.sort(key=len)
    
    answer = []
    check = set()
    for el_list in s_list:
        for el in el_list:
            if el not in check: # answer로 검사하면 비효율. set으로 검사 O(n) -> O(1)
                answer.append(el)
                check.add(el)
    
    return answer