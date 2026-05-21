def solution(polynomial):
    linear = 0
    constant = 0
    for term in polynomial.split(' + '):
        if 'x' in term:
            linear += 1 if term == 'x' else int(term[:-1])
        else:
            constant += int(term)
    
    answer = []
    if linear > 0:
        answer.append('x' if linear == 1 else f'{linear}x')
    if constant > 0:
        answer.append(str(constant))
    
    return ' + '.join(answer)