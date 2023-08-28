import sys
from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def throw(direction, height):
    if direction == 0: #왼쪽에서 오른쪽으로
        y = -1
        for c in range(C):
            y += 1
            if board[height][y] == 'x':
                board[height][y] = '.'
                break
    elif direction == 1: #오른쪽에서 왼쪽으로
        y = C
        for c in range(C):
            y -= 1
            if board[height][y] == 'x':
                board[height][y] = '.'
                break

def bfs_cluster():
    global visit
    queue = deque([])
    clusters = dict()

    cnum = 1 #cluster number
    for r in range(R):
        for c in range(C):
            if visit[r][c] == -1:
                if board[r][c] == 'x':
                    queue.append((r, c)); visit[r][c] = cnum
                    while queue:
                        x, y = queue.popleft()
                        for i in range(4):
                            nx = x + dx[i]; ny = y + dy[i]
                            if 0 <= nx < R and 0 <= ny < C:
                                if board[nx][ny] == 'x' and visit[nx][ny] == -1:
                                    queue.append((nx, ny)); visit[nx][ny] = cnum
                    cnum += 1

    for r in range(R):
        for c in range(C):
            if visit[r][c] != -1:
                if visit[r][c] in clusters:
                    clusters[visit[r][c]].append((r, c))
                else:
                    clusters[visit[r][c]] = [(r, c)]

    return clusters

def gravity(clusters):
    global visit
    distance = {i: int(10e9) for i in range(1, max(clusters.keys()) + 1)} #각 cluster가 내려와야할 거리

    # distance 완성해주기
    for r in range(R):
        for c in range(C):
            if board[r][c] == 'x':
                
                x = r-1; y = c; cnt = 1; flag = False
                while 0 <= x < R:
                    if board[x][y] == 'x':
                        flag = True; break
                    x -= 1; cnt += 1
                
                if flag and visit[x][y] != visit[r][c]:
                    distance[visit[x][y]] = min(distance[visit[x][y]], cnt)

    # distance만큼 cluster 내려주기
    for key, value in clusters.items(): # key는 cluster number, value는 [(x1, y1), (x2, y2) ... ]
        value.sort(reverse = True)
        if value[0][0] == R-1: continue #바닥에 붙어 있는 cluster

        for x, y in value:
            distance[key] = min(distance[key], R - x) #예외처리: 공중에 떠있는 cluster (바닥으로 떨어지는 경우)
            if distance[key] != int(10e9):
                nx = x + distance[key] - 1; ny = y
                board[x][y] = '.'; board[nx][ny] = 'x'


R, C = map(int, sys.stdin.readline()[:-1].split())
board = []
for r in range(R):
    board.append(list(sys.stdin.readline()[:-1]))
N = int(sys.stdin.readline()[:-1])
sticks = list(map(int, sys.stdin.readline().strip().split()))

for n in range(N):
    throw(n % 2, R - sticks[n])

    visit = [[-1] * C for _ in range(R)] #visit에 cluster number를 기록
    clusters = bfs_cluster()
    gravity(clusters)

for i in range(R):
    print(''.join(map(str, board[i])))