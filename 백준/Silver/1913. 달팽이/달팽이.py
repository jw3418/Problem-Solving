import sys
input = sys.stdin.readline

N = int(input()); M = int(input())
arr = [[0]*N for n in range(N)]

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

cnt = N*N
d = 0
x, y = 0, 0
tx, ty = 0, 0
while cnt > 0:
    arr[x][y] = cnt
    if cnt == M: tx = x+1; ty = y+1
    
    if x+dx[d]<0 or x+dx[d]>=N or y+dy[d]<0 or y+dy[d]>=N or arr[x+dx[d]][y+dy[d]] != 0:
        d = (d+1)%4

    x = x+dx[d]
    y = y+dy[d]
    cnt -= 1

for li in arr: print(*li)
print(tx, ty)