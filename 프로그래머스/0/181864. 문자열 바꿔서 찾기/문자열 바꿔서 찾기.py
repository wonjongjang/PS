def solution(myString, pat):
    temp = ''
    for ch in myString:
        if ch == 'A':
            temp += 'B'
        else:
            temp += 'A'
    
    return 1 if pat in temp else 0



# def solution(myString, pat):
#     changed = myString.translate(str.maketrans('AB', 'BA'))
#     return 1 if pat in changed else 0