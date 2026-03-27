def solution(genres, plays):
    genres_total = {}
    genres_songs = {}
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genres_total[genre] = genres_total.get(genre, 0) + play
        
        if genre not in genres_songs:
            genres_songs[genre] = []
        genres_songs[genre].append((play, i))
    
    sorted_genres = sorted(genres_total.keys(), key=lambda x:genres_total[x], reverse=True)
    
    answer = []
    
    for genre in sorted_genres:
        songs = genres_songs[genre]
        songs.sort(key=lambda x: (-x[0], x[1])) # 튜플 정렬은 작성 순서대로 비교

        for play, i in songs[:2]:
            answer.append(i)
        
    return answer

# zip() : 여러 개의 리스트를 같은 위치끼리 묶어주는 함수 (iterable)
# enumerate() : 반복할 때 인덱스를 같이 주는 함수
