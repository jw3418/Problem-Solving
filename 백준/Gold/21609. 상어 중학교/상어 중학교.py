import sys
from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def gravity(board):
    for i in range(N-2, -1, -1):
        for j in range(N):
            if board[i][j] != -1 and board[i][j] != -2:
                r = i
                while True:
                    if 0 <= r+1 < N and board[r+1][j] == -2:
                        board[r+1][j] = board[r][j]; board[r][j] = -2
                        r += 1
                    else:
                        break

def bfs_find(x, y, standard_color):
    queue = deque([]); queue.append((x, y))
    visit[x][y] = True

    rainbow_nodes = []
    normal_nodes = [(x, y)]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == standard_color and not visit[nx][ny]:
                    visit[nx][ny] = True
                    queue.append((nx, ny))
                    normal_nodes.append((nx, ny))
                elif board[nx][ny] == 0 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    queue.append((nx, ny))
                    rainbow_nodes.append((nx, ny))

    for x, y in rainbow_nodes: #무지개블록은 방문을 다시 해제해줘야함!
        visit[x][y] = False

    return [len(normal_nodes + rainbow_nodes), len(rainbow_nodes), normal_nodes + rainbow_nodes]

def bfs_remove(group):
    global total_score
    total_score += group[0] ** 2

    for x, y in group[2]:
        board[x][y] = -2


N, M = map(int, sys.stdin.readline()[:-1].split())
board = []
for n in range(N):
    board.append(list(map(int, sys.stdin.readline()[:-1].split())))

total_score = 0
while True:
    # 크기가 가장 큰 블록 그룹 찾기
    groups = []
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and not visit[i][j]: #일반블록부터 탐색을 시작해야함!
                group = bfs_find(i, j, board[i][j])
                if group[0] >= 2:
                    groups.append(group)
    groups.sort(reverse = True)

    if not groups: #블록 그룹 없음 -> 종료
        break

    # 찾은 블록 그룹의 모든 블록 제거 + 점수 획득
    bfs_remove(groups[0])

    # 중력 작용
    gravity(board)
                
    # 반시계방향 90도 회전
    board = list(reversed(list(map(list, zip(*board)))))

    # 다시 중력 작용
    gravity(board)

print(total_score)