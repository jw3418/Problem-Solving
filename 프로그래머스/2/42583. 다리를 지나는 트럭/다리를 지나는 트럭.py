from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights); queue = deque([])
    
    cnt = 0; sum_ = 0
    while truck_weights:
        if len(queue) == bridge_length:
            sum_ -= queue.popleft()
        if len(queue) < bridge_length:
            if sum_ + truck_weights[0] <= weight:
                tmp = truck_weights.popleft()
                queue.append(tmp)
                sum_ += tmp
            else:
                queue.append(0)
        cnt += 1
    cnt += bridge_length
    
    return cnt