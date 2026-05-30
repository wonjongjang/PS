def solution(babbling):
    answer = 0
    
    for word in babbling:
        for pron in ["aya", "ye", "woo", "ma"]:
            word = word.replace(pron, ' ')
        
        if not word.strip():
            answer += 1
    
    return answer