import sys
from collections import deque
input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

N = int(input())
board = [list(map(int, input().strip().split())) for n in range(N)]
min_ = min(min(row) for row in board)
max_ = max(max(row) for row in board)

def can_reach(diff):
    global min_, max_
    for min_val in range(min_, max_ - diff + 1):
        max_val = min_val + diff
        if bfs(min_val, max_val): return True
    return False

def bfs(min_val, max_val):
    global N
    if board[0][0] < min_val or board[0][0] > max_val: return False
    
    queue = deque([]); queue.append((0, 0))
    visited = [[False]*N for n in range(N)]; visited[0][0] = True
    while queue:
        x, y = queue.popleft()
        if (x, y) == (N-1, N-1): return True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if not visited[nx][ny] and min_val <= board[nx][ny] <= max_val:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return False

left, right = 0, max_ - min_
answer = right
while left <= right:
    mid = (left + right) // 2
    if can_reach(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
print(answer)