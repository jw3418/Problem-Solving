import sys
from collections import deque

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, sys.stdin.readline()[:-1].split())
A = [] #각 위치 별 물의 양
for n in range(N):
    A.append(list(map(int, sys.stdin.readline()[:-1].split())))

cmd = []
for m in range(M):
    cmd.append(list(map(int, sys.stdin.readline()[:-1].split())))

clouds = deque([[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]])
for m in range(M):
    d, s = cmd[m]; d -= 1

    for cloud in clouds:
        cloud[0] += dx[d] * s; cloud[1] += dy[d] * s
        cloud[0] = cloud[0] % N; cloud[1] = cloud[1] % N
        A[cloud[0]][cloud[1]] += 1
    
    for cloud in clouds:
        x, y = cloud; cnt = 0
        for i in range(1, 8, 2):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if A[nx][ny] != 0:
                    cnt += 1
        A[x][y] += cnt 
    
    check = clouds.copy()
    for i in range(len(check)):
        check[i] = tuple(check[i])
    check = set(check)
    clouds.clear()
    for i in range(N):
        for j in range(N):
            if A[i][j] >= 2 and (i, j) not in check:
                clouds.append([i, j])
                A[i][j] -= 2

result = 0
for i in range(N):
    result += sum(A[i])
print(result)