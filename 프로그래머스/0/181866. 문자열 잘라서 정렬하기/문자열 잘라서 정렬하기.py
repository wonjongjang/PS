def solution(myString):
    return sorted(filter(None ,myString.split('x')))



# def solution(myString):
#     return sorted(s for s in myString.split('x') if s)