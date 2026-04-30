def solution(myString):
    answer = []
    
    for ch in myString:
        if ch < 'l':
            answer.append('l')
        else:
            answer.append(ch)
        
    return ''.join(answer)



# def solution(myString):
#     return ''.join(ch if ch >= 'l' else 'l' for ch in myString)