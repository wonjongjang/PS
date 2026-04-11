import re

def solution(files):
    temp = []
    
    for file in files:
        f = re.split(r'(\d+)', file)
        temp.append([f[0], f[1], ''.join(f[2:])])
    
    temp.sort(key=lambda x: (x[0].upper(), int(x[1])))
    
    return [''.join(t) for t in temp]

# import re

# def solution(files):
#     temp = []
    
#     for file in files:
#         head, number, *tail = re.split(r'(\d+)', file)
#         temp.append((head, int(number), file))
    
#     temp.sort(key=lambda x: (x[0].lower(), x[1]))
    
#     return [x[2] for x in temp]