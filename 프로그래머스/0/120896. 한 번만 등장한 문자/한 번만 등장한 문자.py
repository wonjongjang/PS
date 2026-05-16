from collections import Counter

def solution(s):
    counter = Counter(s)

    return ''.join(sorted(ch for ch, count in counter.items() if count == 1))