import sys


N, M = map(int, sys.stdin.readline()[:-1].split())
dist = [[0 for _ in range(N+1)] for _ in range(N+1)]
for m in range(M):
    a, b = map(int, sys.stdin.readline()[:-1].split()); dist[a][b] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if dist[i][j] == 1 or (dist[i][k] == 1 and dist[k][j] == 1):
                dist[i][j] = 1

answer = 0
for i in range(1, N+1):
    tmp = 0
    for j in range(1, N+1):
        tmp += dist[i][j] + dist[j][i]
    if tmp == N-1: answer += 1
print(answer)