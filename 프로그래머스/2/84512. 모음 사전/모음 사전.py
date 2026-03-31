from itertools import permutations

def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    answer = 0
    
    def dfs(char):
        nonlocal answer
        
        if char == word:
            return True
        
        if len(char) == 5:
            return
        
        for i in range(5):
            answer += 1
            if dfs(char + alpha[i]):
                return True
            
        return False
    
    dfs('')
    
    return answer


# def solution(word):
#     weights = [781, 156, 31, 6, 1]
#     vowels = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4} # 사전 순서에 의한 모음 번호
    
#     answer = 0
#     for i, ch in enumerate(word):
#         answer += vowels[ch] * weights[i] + 1
    
#     return answer

# 가중치는 뒤에 올 수 있는 경우의 수를 모두 더한 값
# 첫째 자리: 1 + 5 + 25 + 125 + 625 = 781
# 둘째 자리: 1 + 5 + 25 + 125 = 156
# 셋째 자리: 1 + 5 + 25 = 31
# 넷째 자리: 1 + 5 = 6
# 다섯째 자리: 1