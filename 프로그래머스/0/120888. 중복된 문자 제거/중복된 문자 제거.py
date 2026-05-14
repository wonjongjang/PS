def solution(my_string):
    check = set()
    answer = []
    
    for ch in my_string:
        if ch not in check:
            check.add(ch)
            answer.append(ch)
    
    return ''.join(answer)