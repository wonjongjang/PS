def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    answer = []
    
    for e in emergency:
        answer.append(sorted_emergency.index(e) + 1)
    
    return answer