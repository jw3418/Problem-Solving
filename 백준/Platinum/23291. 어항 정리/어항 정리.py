import sys
from collections import deque
import copy

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

N, K = map(int, sys.stdin.readline()[:-1].split())
bowl = list(map(int, sys.stdin.readline()[:-1].split()))

count = 0
while max(bowl) - min(bowl) > K:
    ##### 물고기 수 가장 적은 어항에 물고기 한마리 넣기
    min_bowl = min(bowl)
    for i in range(N):
        if bowl[i] == min_bowl: bowl[i] += 1

    ##### 공중 부양 후 시계방향 90도
    tbowl = deque([])
    tbowl.append(deque([bowl[0]])); tbowl.append(deque(bowl[1:]))
    
    while True:
        height = len(tbowl); width = len(tbowl[0])
        if len(tbowl[-1]) - width < height: break 
        
        will_turn = []
        for h in range(height):
            tmp = []
            for w in range(width):
                tmp.append(tbowl[h].popleft())
            will_turn.append(tmp)
        for h in range(height-1): #비어있는 deque 제거
            tbowl.popleft()

        will_turn = reversed(will_turn); will_turn = list(map(list, zip(*will_turn))) #시계방향 90도 회전

        for i in range(len(will_turn)-1, -1, -1):
            tbowl.appendleft(deque(will_turn[i]))
    
    ##### 인접한 두 어항에 대한 처리
    changed_tbowl = copy.deepcopy(tbowl)
    R = len(tbowl)
    visit = [[False]*len(tbowl[-1]) for _ in range(R)]
    for x in range(R):
        for y in range(len(tbowl[x])):
            visit[x][y] = True
            for i in range(4):
                nx = x + dx[i]; ny = y + dy[i]
                if 0 <= nx < R and 0 <= ny < len(tbowl[nx]):
                    if not visit[nx][ny]:
                        d = abs(tbowl[x][y] - tbowl[nx][ny]) // 5
                        if d > 0:
                            if tbowl[x][y] > tbowl[nx][ny]:
                                changed_tbowl[x][y] -= d; changed_tbowl[nx][ny] += d
                            else:
                                changed_tbowl[x][y] += d; changed_tbowl[nx][ny] -= d

    tbowl = changed_tbowl #aliasing

    ##### 바닥에 일렬로 놓기
    bowl = []
    for c in range(len(tbowl[-1])):
        for h in range(len(tbowl)-1, -1, -1):
            if tbowl[h]: bowl.append(tbowl[h].popleft())
    tbowl = deque([]); tbowl.append(deque(bowl))

    ##### 다시 공중 부양 작업 (시계 방향 180도 회전)
    for _ in range(1, 3):
        will_turn = []
        for h in range(len(tbowl)):
            tmp = []
            for w in range(N//(2*_)):
                tmp.append(tbowl[h].popleft())
            will_turn.append(tmp)

        will_turn = reversed(will_turn); will_turn = list(map(list, zip(*will_turn))) #시게방향 90도 회전
        will_turn = reversed(will_turn); will_turn = list(map(list, zip(*will_turn))) #시계방향 90도 회전
        
        for i in range(len(will_turn)-1, -1, -1):
            tbowl.appendleft(deque(will_turn[i]))

    ##### 다시 인접한 두 어항에 대한 처리
    changed_tbowl = copy.deepcopy(tbowl)
    R = len(tbowl)
    visit = [[False]*len(tbowl[-1]) for _ in range(R)]
    for x in range(R):
        for y in range(len(tbowl[x])):
            visit[x][y] = True
            for i in range(4):
                nx = x + dx[i]; ny = y + dy[i]
                if 0 <= nx < R and 0 <= ny < len(tbowl[nx]):
                    if not visit[nx][ny]:
                        d = abs(tbowl[x][y] - tbowl[nx][ny]) // 5
                        if d > 0:
                            if tbowl[x][y] > tbowl[nx][ny]:
                                changed_tbowl[x][y] -= d; changed_tbowl[nx][ny] += d
                            else:
                                changed_tbowl[x][y] += d; changed_tbowl[nx][ny] -= d

    tbowl = changed_tbowl #aliasing

    ##### 바닥에 일렬로 놓기
    bowl = []
    for c in range(len(tbowl[-1])):
        for h in range(len(tbowl)-1, -1, -1):
            if tbowl[h]: bowl.append(tbowl[h].popleft())
    
    count += 1
    
print(count)