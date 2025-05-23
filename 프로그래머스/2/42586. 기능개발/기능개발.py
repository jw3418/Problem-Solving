from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses); speeds = deque(speeds)
    
    result = []
    while progresses:
        
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft(); speeds.popleft()
            cnt += 1
        if cnt != 0: result.append(cnt)
    return result