import sys
from collections import deque
import copy
sys.setrecursionlimit(10**6)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, color):
    if x < 0 or y < 0 or x >= N or y >= N:
        return

    if grid[x][y] == color:
        grid[x][y] = 0
        for i in range(4):
            dfs(x + dx[i], y + dy[i], color)

def dfs_B(x, y, color):
    if x < 0 or y < 0 or x >= N or y >= N:
        return

    if origin_grid[x][y] == color:
        origin_grid[x][y] = 0
        for i in range(4):
            dfs_B(x + dx[i], y + dy[i], color)
                
def dfs_RG(x, y, color):
    if x < 0 or y < 0 or x >= N or y >= N:
        return
    
    if origin_grid[x][y] == 'R' or origin_grid[x][y] == 'G':
        origin_grid[x][y] = 0
        for i in range(4):
            dfs_RG(x + dx[i], y + dy[i], color)
                

N = int(input())
origin_grid = []
for n in range(N):
    origin_grid.append(list(sys.stdin.readline()[:-1]))

grid = copy.deepcopy(origin_grid)
normal_count = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] != 0:
            dfs(i, j, grid[i][j])
            normal_count += 1

abnormal_count = 0
for i in range(N):
    for j in range(N):
        if origin_grid[i][j] == 'B':
            dfs_B(i, j, origin_grid[i][j])
            abnormal_count += 1
        elif origin_grid[i][j] == 'R' or origin_grid[i][j] == 'G':
            dfs_RG(i, j, origin_grid[i][j])
            abnormal_count += 1

print(normal_count, abnormal_count)