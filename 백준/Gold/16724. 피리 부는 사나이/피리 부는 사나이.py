import sys

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

N, M = map(int, sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for n in range(N)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a); b = find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

parent = [i for i in range(N*M)]
for idx in range(N*M): #find-union 수행
    x = idx//M; y = idx%M
    direction = -1
    if board[x][y] == 'D': direction = 3
    elif board[x][y] == 'U': direction = 2
    elif board[x][y] == 'R': direction = 1
    elif board[x][y] == 'L': direction = 0

    nx, ny = x + dx[direction], y + dy[direction]
    if 0<=nx<N and 0<=ny<M:
        nidx = nx*M + ny
        if find(idx) != find(nidx): union(idx, nidx)

for idx in range(N*M): find(idx)
print(len(set(parent)))