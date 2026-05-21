def solution(spell, dic):
    target = set(spell)
    
    for word in dic:
        if target == set(word):
            return 1
    
    return 2