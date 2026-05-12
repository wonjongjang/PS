def solution(box, n):
    w, d, h = box
    
    return (w // n) * (d // n) * (h // n)