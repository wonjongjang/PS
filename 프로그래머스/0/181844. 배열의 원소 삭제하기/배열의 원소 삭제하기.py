def solution(arr, delete_list):
    delete = set(delete_list)
    return [n for n in arr if n not in delete]