def solution(myStr):
    answer = myStr.translate(str.maketrans('abc', '   ')).split()
    return answer if answer else ['EMPTY']