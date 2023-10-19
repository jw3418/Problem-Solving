import sys

#동서남북
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

def dfs(x, y, depth, prob):
    global answer
    if depth == N:
        answer += prob
        return

    for i in range(4):
        nx = x+dx[i]; ny = y+dy[i]
        if 0<=nx<(2*N+1) and 0<=ny<(2*N+1):
            if not visit[nx][ny]:
                visit[nx][ny] = True
                dfs(nx, ny, depth+1, prob*direction_prob[i])
                visit[nx][ny] = False #방문 해제

N, e, w, s, n = map(int, sys.stdin.readline().strip().split())
direction_prob = [e/100, w/100, s/100, n/100]

visit = [[False]*(2*N+1) for n in range(2*N+1)]

answer = 0
visit[N][N] = True
dfs(N, N, 0, 1)
print(answer)