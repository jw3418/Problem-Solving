import sys
from collections import deque
input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

N, K = map(int, input().split())
board = [list(map(int, list(input().strip()))) for n in range(N)]

while True:
    ### 중력 작용
    for j in range(10):
        blocks = []
        for i in range(N):
            if board[i][j] != 0: blocks.append(board[i][j])
        for i in range(N-1, -1, -1):
            if blocks: board[i][j] = blocks.pop()
            else: board[i][j] = 0

    ### 크기 K이상인 영역 찾기
    visit = [[False]*10 for n in range(N)]
    result = []
    for i in range(N):
        for j in range(10):
            if board[i][j] != 0 and not visit[i][j]:
                queue = deque([]); queue.append((i, j))
                visit[i][j] = True
                color = board[i][j]; tresult = []
                while queue:
                    x, y = queue.popleft()
                    tresult.append((x, y))
                    for d in range(4):
                        nx, ny = x+dx[d], y+dy[d]
                        if 0<=nx<N and 0<=ny<10:
                            if board[nx][ny] == color and not visit[nx][ny]:
                                visit[nx][ny] = True
                                queue.append((nx, ny))
                if len(tresult) >= K: result.extend(tresult)

    # 제거 대상 영역 없으면 종료
    if not result: break

    ### 찾은 크기 K이상인 영역 제거
    for x, y in result: board[x][y] = 0
for i in range(N): print("".join(map(str, board[i])))