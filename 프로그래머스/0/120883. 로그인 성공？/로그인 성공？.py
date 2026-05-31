def solution(id_pw, db):
    for db_id, db_pw in db:
        if db_id == id_pw[0]:
            if db_pw == id_pw[1]:
                return "login"
            else:
                return "wrong pw"
            
    return "fail"



# def solution(id_pw, db):
#     user_id, user_pw = id_pw
    
#     # 1. 2차원 배열 형태의 db를 딕셔너리(Map) 형태로 변환합니다.
#     db_dict = dict(db)
    
#     # 2. 딕셔너리 키(Key) 중에 입력한 아이디가 있는지 확인합니다.
#     if user_id in db_dict:
#         # 3. 아이디가 있다면, 값(Value)인 비밀번호가 일치하는지 확인합니다.
#         return "login" if db_dict[user_id] == user_pw else "wrong pw"
        
#     # 4. 아이디 자체가 없다면 fail을 반환합니다.
#     return "fail"