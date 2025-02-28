import sys
from collections import deque
input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

N, M = map(int, input().split())
info = dict()
for m in range(M):
    x, y, a, b = map(int, input().split()); x-=1; y-=1; a-=1; b-=1
    if (x, y) not in info: info[(x, y)] = [(a, b)]
    else: info[(x, y)].append((a, b))

queue = deque([]); queue.append((0, 0))
visit = [[False]*N for n in range(N)]; visit[0][0] = True
light = [[False]*N for n in range(N)]; light[0][0] = True
cnt = 1
while queue:
    x, y = queue.popleft()
    if (x, y) in info:
        for lx, ly in info[(x, y)]:
            if not light[lx][ly]:
                light[lx][ly] = True
                cnt += 1
                '''이전 시점에 불이 안켜져 있어서 지나가지 못했던 곳도 탐색 해줘야함!'''
                for i in range(4):
                    nx, ny = lx+dx[i], ly+dy[i]
                    if 0<=nx<N and 0<=ny<N:
                        if visit[nx][ny]:
                            queue.append((nx, ny))
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<N:
            if not visit[nx][ny] and light[nx][ny]:
                queue.append((nx, ny))
                visit[nx][ny] = True
print(cnt)