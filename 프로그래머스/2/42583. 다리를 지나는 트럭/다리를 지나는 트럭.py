from collections import deque

def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    
    time = 0
    current_weight = 0
    
    while trucks or current_weight > 0:
        current_weight -= bridge.popleft()
        
        if trucks and current_weight + trucks[0] <= weight:
            truck = trucks.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            bridge.append(0)
            
        time += 1
        
    return time