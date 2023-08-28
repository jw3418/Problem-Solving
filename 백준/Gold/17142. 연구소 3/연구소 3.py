import sys
from collections import deque
from itertools import combinations

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(start):
    queue = deque(start)
    visit = [[-1 for _ in range(N)] for _ in range(N)]
    for i in range(M):
        visit[start[i][0]][start[i][1]] = 0
    
    local_result = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visit[nx][ny] == -1 and board[nx][ny] == 0:
                    visit[nx][ny] = visit[x][y] + 1
                    local_result = max(local_result, visit[x][y] + 1)
                    queue.append([nx, ny])
                elif visit[nx][ny] == -1 and board[nx][ny] == 2: #비활성 바이러스인 경우도 벽이 아니기 때문에 지나갈 수 있음
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append([nx, ny])

    for i in range(N):
        for j in range(N):
            if visit[i][j] == -1 and board[i][j] == 0:
                return 10e9
    return local_result


N, M = map(int, sys.stdin.readline()[:-1].split())
board = []; candidate = []
for n in range(N):
    tmp = list(map(int, sys.stdin.readline()[:-1].split()))
    board.append(tmp)
    for i in range(N):
        if tmp[i] == 2:
            candidate.append([n, i])

result = 10e9
for start in combinations(candidate, M):
    result = min(bfs(start), result)

if result == 10e9:
    print(-1)
else:
    print(result)