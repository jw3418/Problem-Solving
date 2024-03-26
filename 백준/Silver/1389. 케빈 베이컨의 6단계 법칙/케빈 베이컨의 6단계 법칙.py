import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mat = [[int(10e9)]*N for n in range(N)]
for m in range(M):
    a, b = map(int, input().split()); a-=1; b-=1
    mat[a][b] = 1; mat[b][a] = 1
for i in range(N):
    for j in range(N):
        if i==j: mat[i][j]=0

for k in range(N):
    for i in range(N):
        for j in range(N):
            mat[i][j] = min(mat[i][j], mat[i][k]+mat[k][j])

score = int(10e9)
ans = 0
for i in range(N):
    tmp = sum(mat[i])
    if tmp < score:
        ans = i
        score = tmp
print(ans+1)