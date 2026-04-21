def solution(arr):
    x = 0
    
    while True:
        prev = arr[:]
        
        for i, n in enumerate(arr):
            if n >= 50 and n % 2 == 0:
                arr[i] //= 2
            elif n < 50 and n % 2 == 1:
                arr[i] = n * 2 + 1
                
        if prev == arr:
            return x
        
        x += 1