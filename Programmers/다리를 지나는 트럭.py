from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_queue = deque([0]*bridge_length)
    truck_queue = deque(truck_weights)
    
    while truck_queue or bridge_queue:
        answer += 1
        bridge_queue.popleft()
        if truck_queue:
            if sum(bridge_queue) + truck_queue[0] <= weight:
                bridge_queue.append(truck_queue.popleft())
            else:
                bridge_queue.append(0)
    
    return answer