def solution(numbers):
    numbers = list(numbers)
    answer = set()
    visited = [False] * len(numbers)
    
    def isPrime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    
    def dfs(num):
        if num:
            value = int(num)
            if isPrime(value):
                answer.add(value)
        
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                dfs(num + numbers[i])
                visited[i] = False
    
    dfs('')
    return len(answer)

# from itertools import permutations

# def is_prime(n):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
    
#     i = 3
#     while i * i <= n:
#         if n % i == 0:
#             return False
#         i += 2
#     return True

# def solution(numbers):
#     candidates = set()
    
#     for length in range(1, len(numbers) + 1):
#         for p in permutations(numbers, length):
#         # list(permutations("17", 1)) -> [('1',), ('7',)]
#             num = int(''.join(p))
#             candidates.add(num)
    
#     answer = 0
#     for num in candidates:
#         if is_prime(num):
#             answer += 1
    
#     return answer