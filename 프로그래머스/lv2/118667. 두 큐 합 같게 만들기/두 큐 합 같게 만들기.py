from collections import deque

def solution(queue1, queue2):
    if (sum(queue1) + sum(queue2)) % 2 == 1: return -1
    
    N = len(queue1)
    queue1 = deque(queue1); queue2 = deque(queue2)
    
    count = 0; sum_queue1 = sum(list(queue1)); sum_queue2 = sum(list(queue2))
    while True:
        if count > N*4: return -1
        if sum_queue1 == sum_queue2: return count
        elif sum_queue1 > sum_queue2:
            one = queue1.popleft(); queue2.append(one)
            sum_queue1 -= one; sum_queue2 += one
            count += 1
        elif sum_queue1 < sum_queue2:
            two = queue2.popleft(); queue1.append(two)
            sum_queue2 -= two; sum_queue1 += two
            count += 1