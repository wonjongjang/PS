def solution(my_string):
    table = str.maketrans('', '', 'aeiou')
    return my_string.translate(table)



# def solution(my_string):
#     return ''.join(ch for ch in my_string if ch not in 'aeiou')