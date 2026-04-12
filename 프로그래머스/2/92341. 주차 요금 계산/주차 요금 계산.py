import math

def solution(fees, records):
    cars = {}
    for record in records:
        time, number, _ = record.split()    # 시각(시:분), 차량 번호, 내역
        h, m = map(int, time.split(':'))  # 시, 분
        t = h * 60 + m  # 시 -> 분 환산
        
        cars.setdefault(number, []).append(t)
        # if number in cars:
        #     cars[number].append(t)
        # else:
        #     cars[number] = [t]
    
    last = 23 * 60 + 59 # 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주
    answer = []
    for car in sorted(cars):
        times = cars[car]
        
        if len(times) % 2:
            times.append(last)
        
        total_time = 0  # 누적 주차 시간
        for i in range(0, len(times), 2):
            total_time += times[i+1] - times[i]
        
        if total_time <= fees[0]:
            total_fee = fees[1]
        else:
            total_fee = fees[1] + math.ceil((total_time - fees[0]) / fees[2]) * fees[3]
                
        answer.append(total_fee)
    
    return answer