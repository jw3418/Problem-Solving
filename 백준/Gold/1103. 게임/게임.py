import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def dfs(x, y, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)

    for i in range(4):
        nx=x+int(board[x][y])*dx[i]; ny=y+int(board[x][y])*dy[i]
        if 0<=nx<N and 0<=ny<M and board[nx][ny] != 'H' and cnt+1>dp[nx][ny]:
            if not visit[nx][ny]:
                dp[nx][ny] = cnt+1
                visit[nx][ny] = True
                dfs(nx, ny, cnt+1)
                visit[nx][ny] = False
            else: #무한루프
                print(-1)
                exit()

N, M = map(int, input().strip().split())
board = []
for n in range(N): board.append(list(input().strip()))

visit = [[False]*M for n in range(N)]
dp = [[0]*M for n in range(N)] #움직인 횟수를 저장
max_cnt = 0

dfs(0, 0, 0)
print(max_cnt+1)