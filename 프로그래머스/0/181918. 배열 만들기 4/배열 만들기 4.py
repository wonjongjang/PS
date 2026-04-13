def solution(arr):
    stk = []
    i = 0
    
    while i < len(arr):
        if stk: # stk에 원소가 있을 때
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            else:
                stk.pop()
        else:   # stk가 빈 배열일 때
            stk.append(arr[i])
            i += 1
        
    return stk