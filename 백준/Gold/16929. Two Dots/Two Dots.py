import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y, color, src_x, src_y, depth):
    if x < 0 or y < 0 or x >= N or y >= M:
        return

    if x == src_x and y == src_y and depth >= 4:
        print('Yes'); exit()
    
    if Map[x][y] == color:
        #print(Map[x][y], x, y)
        Map[x][y] = 0
        for i in range(4):
            dfs(x + dx[i], y + dy[i], color, src_x, src_y, depth+1)
        Map[x][y] = color


N, M = map(int, input().split(' '))
Map = []
for _ in range(N):
    Map.append(list(sys.stdin.readline()[:-1]))

for x in range(N):
    for y in range(M):
        if Map[x][y] != 0:
            dfs(x, y, Map[x][y], x, y, 0)
        else:
            continue
print('No')