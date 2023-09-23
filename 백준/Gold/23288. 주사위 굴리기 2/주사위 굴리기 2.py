import sys
from collections import deque

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

N, M, K = map(int, sys.stdin.readline()[:-1].split())
board = [list(map(int, sys.stdin.readline()[:-1].split())) for _ in range(N)]
dice = [1, 2, 3, 4, 5, 6]

def change_dice(didx):
    d_0 = dice[0]; d_1 = dice[1]; d_2 = dice[2]; d_3 = dice[3]; d_4 = dice[4]; d_5 = dice[5]
    if didx == 0: #동
        dice[0] = d_3; dice[1] = d_1; dice[2] = d_0; dice[3] = d_5; dice[4] = d_4; dice[5] = d_2
    elif didx == 1: #남
        dice[0] = d_1; dice[1] = d_5; dice[2] = d_2; dice[3] = d_3; dice[4] = d_0; dice[5] = d_4
    elif didx == 2: #서
        dice[0] = d_2; dice[1] = d_1; dice[2] = d_5; dice[3] = d_0; dice[4] = d_4; dice[5] = d_3
    elif didx == 3: #북
        dice[0] = d_4; dice[1] = d_0; dice[2] = d_2; dice[3] = d_3; dice[4] = d_5; dice[5] = d_1

def bfs(x, y, check):
    q = deque([]); q.append((x, y))
    visit = [[False]*M for n in range(N)]; visit[x][y] = True
    cnt = 0

    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visit[nx][ny] and board[nx][ny] == check:
                    visit[nx][ny] = True; q.append((nx, ny))
    return cnt


x, y, didx, answer = 0, 0, 0, 0
for k in range(K):
    if x+dx[didx] < 0 or x+dx[didx] >= N or y+dy[didx] < 0 or y+dy[didx] >= M: didx = (didx+2) % 4
    x, y = x + dx[didx], y + dy[didx]

    answer += (bfs(x, y, board[x][y]) * board[x][y]) #점수 획득

    change_dice(didx) #주사위 전개도 변경
    #전개도에 따른 방향 변경
    if dice[5] > board[x][y]: didx = (didx+1) % 4
    elif dice[5] < board[x][y]: didx = (didx+3) % 4
print(answer)