from collections import deque

def check(a, b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
    return diff == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = [False] * len(words)
    queue = deque()
    queue.append((begin, 0))
    
    while queue:
        curr, step = queue.popleft()
        
        if curr == target:
            return step
        
        for i in range(len(words)):
            if not visited[i] and check(curr, words[i]):
                visited[i] = True
                queue.append((words[i], step+1))
            
    return 0

# from collections import deque

# def can_change(a, b):
#     diff = 0
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             diff += 1
#     return diff == 1

# def solution(begin, target, words):
#     if target not in words:
#         return 0

#     visited = [False] * len(words)
#     queue = deque()
#     queue.append((begin, 0))  # (현재 단어, 변환 횟수)

#     while queue:
#         current, step = queue.popleft()

#         if current == target:
#             return step

#         for i in range(len(words)):
#             if not visited[i] and can_change(current, words[i]):
#                 visited[i] = True
#                 queue.append((words[i], step + 1))

#     return 0