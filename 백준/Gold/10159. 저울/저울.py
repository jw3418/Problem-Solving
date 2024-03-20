import sys
input = sys.stdin.readline

N = int(input()); M = int(input())

adj_li = []
for m in range(M):
    tmp = list(map(int, input().split()))
    tmp[0]-=1; tmp[1]-=1
    adj_li.append(tmp)

adj_mat = [[0]*N for n in range(N)]
for i, j in adj_li: adj_mat[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if adj_mat[i][k] and adj_mat[k][j]:
                adj_mat[i][j] = 1

for i in range(N):
    cnt = 0
    for j in range(N):
        if i != j:
            if not adj_mat[i][j] and not adj_mat[j][i]: cnt+=1
    print(cnt)