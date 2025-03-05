import sys
from collections import deque
input = sys.stdin.readline

D = ['U', 'D', 'L', 'R', 'T']

N = int(input())
board = [list(input().strip()) for n in range(N)]

B = []; E = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 'B': B.append((i, j)); board[i][j] = '0'
        elif board[i][j] == 'E': E.append((i, j)); board[i][j] = '0'

def check(pos, direction):
    if direction == 'U':
        for i in range(3):
            x, y = pos[i]; nx, ny = x-1, y
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] != '0': return False
        return True
    elif direction == 'D':
        for i in range(3):
            x, y = pos[i]; nx, ny = x+1, y
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] != '0': return False
        return True
    elif direction == 'L':
        for i in range(3):
            x, y = pos[i]; nx, ny = x, y-1
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] != '0': return False
        return True
    elif direction == 'R':
        for i in range(3):
            x, y = pos[i]; nx, ny = x, y+1
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] != '0': return False
        return True
    elif direction == 'T':
        hori = (pos[0][0] == pos[1][0])
        if hori:
            for i in range(3):
                x, y = pos[i]
                nx, ny = x-1, y
                if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] != '0': return False
                nx, ny = x+1, y
                if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] != '0': return False
            return True
        else:
            for i in range(3):
                x, y = pos[i]
                nx, ny = x, y-1
                if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] != '0': return False
                nx, ny = x, y+1
                if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] != '0': return False
            return True
    return False

def move(cur, direction):
    nex = []
    if direction == 'U':            
        for i in range(3):
            x, y = cur[i]; nex.append((x-1, y))
    if direction == 'D':
        for i in range(3):
            x, y = cur[i]; nex.append((x+1, y))
    if direction == 'L':
        for i in range(3):
            x, y = cur[i]; nex.append((x, y-1))
    if direction == 'R':
        for i in range(3):
            x, y = cur[i]; nex.append((x, y+1))
    if direction == 'T':
        hori = (cur[0][0] == cur[1][0])
        if hori:
            x, y = cur[1]
            nex = [(x-1, y), (x, y), (x+1, y)]
        else:
            x, y = cur[1]
            nex = [(x, y-1), (x, y), (x, y+1)]
    return nex

queue = deque([]); queue.append([B, 0])
visit = set(); visit.add(tuple(B))
while queue:
    cur_b, cnt = queue.popleft()
    if cur_b == E: print(cnt); exit()
    for d in D:
        if check(cur_b, d):
            nex_b = move(cur_b, d)
            if tuple(nex_b) not in visit:
                visit.add(tuple(nex_b))
                queue.append([nex_b, cnt+1])
print(0)