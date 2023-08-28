import sys
from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def partition(x, y, color):
    queue = deque([]); queue.append((x, y))
    visit[x][y] = True
    board[x][y] = color

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] != 0 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    board[nx][ny] = color
                    queue.append((nx, ny))

def bridge(x, y, color):
    queue = deque([])
    queue.append((x, y, 'r', 0))
    queue.append((x, y, 'c', 0))

    visit = [[False] * M for _ in range(N)]
    visit[x][y] = True

    while queue:
        x, y, direction, cnt = queue.popleft() #가로는 'r', 세로는 'c'
        if direction == 'r':
            for i in range(2):
                nx = x + dx[i]; ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if board[nx][ny] == 0 and not visit[nx][ny]:
                        visit[nx][ny] = True
                        queue.append((nx, ny, direction, cnt+1))
                    elif board[nx][ny] != 0 and board[nx][ny] != color:
                        if cnt >= 2:
                            bridges.add((color, board[nx][ny], cnt))
        elif direction == 'c':
            for i in range(2, 4):
                nx = x + dx[i]; ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if board[nx][ny] == 0 and not visit[nx][ny]:
                        visit[nx][ny] = True
                        queue.append((nx, ny, direction, cnt+1))
                    elif board[nx][ny] != 0 and board[nx][ny] != color:
                        if cnt >= 2:
                            bridges.add((color, board[nx][ny], cnt))


N, M = map(int, sys.stdin.readline()[:-1].split())
board = []
for n in range(N):
    board.append(list(map(int, sys.stdin.readline()[:-1].split())))

##### 섬 구분하기
visit = [[False] * M for _ in range(N)]
color = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and not visit[i][j]:
            color += 1
            partition(i, j, color)

##### 다리 구하기
bridges = set()
for i in range(N):
    for j in range(M):
        if board[i][j] != 0:
            bridge(i, j, board[i][j])

##### Minimum Spanning Tree 구하기 (Kruskal 알고리즘 이용)
'''
1. 주어진 모든 bridge에 대해 cost가 낮은 순서로 정렬
2. 정렬된 bridges를 하나씩 확인하면서 현재의 bridge가 섬 간의 사이클을 발생시키는 지 확인
3. 사이클이 발생하지 않은 경우 Minimun Spanning Tree에 포함시키고/ 사이클이 발생한 경우 Minimum Spanning Tree에 포함시키지 않음
4. 1~3의 과정을 모든 bridge에 대해 반복 수행
'''
bridges = list(bridges)
bridges.sort(key=lambda x:x[2])

def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

parent = [i for i in range(color+1)]
total_cost = 0; check = 0
for a, b, cost in bridges:
    if find_parent(parent, a) != find_parent(parent, b): # 부모노드가 다른 경우 -> 사이클 발생하지 않음 -> MST에 포함
        union_parent(parent, a, b)
        total_cost += cost
        check += 1

if check != color-1:
    print(-1)
else:
    print(total_cost) 