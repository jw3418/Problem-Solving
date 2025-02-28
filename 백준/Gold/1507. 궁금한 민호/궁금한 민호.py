import sys
input = sys.stdin.readline

N = int(input())
adj_mat = []
for n in range(N): adj_mat.append(list(map(int, input().split())))

edges = [[1 for j in range(N)] for i in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j: edges[i][j] -= 1
            elif i == k or j == k: continue
            elif adj_mat[i][j] == adj_mat[i][k] + adj_mat[k][j]: edges[i][j] -= 1
            elif adj_mat[i][j] > adj_mat[i][k] + adj_mat[k][j]: print(-1); exit()
ans = 0
for i in range(N):
    for j in range(i, N):
        if edges[i][j] == 1: ans += adj_mat[i][j]
print(ans)