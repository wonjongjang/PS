def solution(quiz):
    answer = []
    
    for q in quiz:
        x, op, y, eq, z = q.split()
        
        if op == '+':
            answer.append('O' if int(x) + int(y) == int(z) else 'X')
        else:
            answer.append('O' if int(x) - int(y) == int(z) else 'X')
            
    return answer