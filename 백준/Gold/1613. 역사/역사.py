import sys
input = sys.stdin.readline

N, K = map(int, input().split())

mat = [[0]*N for n in range(N)]
for k in range(K):
    a, b = map(int, input().split())
    a-=1; b-=1
    mat[a][b] = 1 #a 다음 b 일어남

for k in range(N):
    for i in range(N):
        for j in range(N):
            if mat[i][k] and mat[k][j]:
                mat[i][j] = 1

S = int(input())
for s in range(S):
    a, b = map(int, input().split())
    a-=1; b-=1
    if mat[a][b] or mat[b][a]:
        if mat[a][b]: print(-1)
        else: print(1)
    else:
        print(0)