def solution(numbers, k):
    i = 0
    count = 1
    
    while count != k:
        i = (i + 2) % len(numbers)
        count += 1
    
    return numbers[i]



# def solution(numbers, k):
#     return numbers[2 * (k - 1) % len(numbers)]