import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def bfs(start, board, N, M):
    queue = deque([start])
    visited = [[-1]*M for _ in range(N)]
    visited[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if visited[nx][ny] == -1 and board[nx][ny] != 'x':
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    return visited

while True:
    M, N = map(int, input().strip().split())
    if (N, M) == (0, 0): break

    board = []
    for n in range(N): 
        board.append(list(input().strip()))

    start = None
    dirty = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'o': 
                start = (i, j)
            elif board[i][j] == '*': 
                dirty.append((i, j))
    
    if not dirty:
        print(0)
        continue
    
    # 모든 지점(시작점 + 더러운 칸들) 간의 거리 계산
    points = [start] + dirty
    dist = {}
    # 각 지점에서 다른 모든 지점까지의 거리 계산
    for point in points:
        distances = bfs(point, board, N, M)
        dist[point] = distances
    
    # 방문할 수 없는 더러운 칸이 있는지 확인
    impossible = False
    for d in dirty:
        if dist[start][d[0]][d[1]] == -1:
            impossible = True
            break
    if impossible:
        print(-1)
        continue
    
    ans = int(10e9)
    for perm in permutations(dirty):
        total_distance = 0
        cur = start
        
        for nex in perm:
            distance = dist[cur][nex[0]][nex[1]]
            if distance == -1:  # 도달할 수 없으면
                total_distance = int(10e9)
                break
            total_distance += distance
            cur = nex
        
        ans = min(ans, total_distance)
    
    if ans == int(10e9): print(-1)
    else: print(ans)