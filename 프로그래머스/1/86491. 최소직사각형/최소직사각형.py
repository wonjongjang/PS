def solution(sizes):
    ns = []
    for w, h in sizes:
        if w > h:
            ns.append((w, h))
        else:
            ns.append((h, w))
            
    max_w = max([w for w, h in ns])
    max_h = max([h for w, h in ns])
    
    return max_w * max_h

# def solution(sizes):
#     max_w = 0
#     max_h = 0

#     for w, h in sizes:
#         big = max(w, h)
#         small = min(w, h)

#         max_w = max(max_w, big)
#         max_h = max(max_h, small)

#     return max_w * max_h