from collections import deque

def solution(priorities, location):
    
    li = deque([])
    for i in range(len(priorities)): li.append((i, priorities[i]))
    
    cnt = 0
    while li:
        tmp = li.popleft()
        for i in range(len(li)):
            if li[i][1] > tmp[1]:
                li.append(tmp)
                break
        else:
            cnt += 1
            if tmp[0] == location:
                return cnt