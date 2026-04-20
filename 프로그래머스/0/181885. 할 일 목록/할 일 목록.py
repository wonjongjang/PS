def solution(todo_list, finished):
    answer = []
    for todo, f in zip(todo_list, finished):
        if not f:
            answer.append(todo)
    return answer

# def solution(todo_list, finished):
#     return [todo for todo, done in zip(todo_list, finished) if not done]