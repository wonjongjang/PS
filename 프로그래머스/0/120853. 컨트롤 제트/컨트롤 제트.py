def solution(s):
    stack = []
    
    for x in s.split():
        if x == 'Z':
            stack.pop()
        else:
            stack.append(int(x))
    
    return sum(stack)