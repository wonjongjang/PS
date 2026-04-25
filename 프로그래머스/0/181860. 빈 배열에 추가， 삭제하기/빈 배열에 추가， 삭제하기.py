def solution(arr, flag):
    answer = []
    
    for num, boolean in zip(arr, flag):
        if boolean:
            answer.extend([num] * (num * 2))
        else:
            del answer[-num:]

    return answer