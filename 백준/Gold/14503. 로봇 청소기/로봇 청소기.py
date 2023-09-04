tmp = list(map(int, input().split(' ')))
N = tmp[0]; M = tmp[1]
tmp = list(map(int, input().split(' ')))
r = tmp[0]; c = tmp[1]; d = tmp[2] # 0:북, 1:동, 2:남, 3:서
board = []
for _ in range(N):
    board.append(list(map(int, input().split(' ')))) # 0:청소안됨, 1:벽

visited = [[0] * M for _ in range(N)] # 0:청소 안함, 1: 청소 함
visited[r][c] = 1
dx = [-1, 0, 1, 0] #북, 동, 남, 서 순서임
dy = [0, 1, 0, -1] #북, 동, 남, 서 순서임

while True:
    flag = 0
    for i in range(4): #상하좌우 검사/ flag가 0이면 주변 4칸 중 청소되지 않은 빈칸이 없는 거/ flag가 1이면 주변 4칸 중 청소되지 않은 빈칸이 있는 거
        x = r; y = c
        d = (d+3)%4
        x += dx[d]; y += dy[d]     
        if x >= 0 and x < N and y >= 0 and y < M:
            if board[x][y] == 0 and visited[x][y] == 0:
                visited[x][y] = 1
                r = x; c = y
                flag = 1; break
    
    if flag == 0:
        r  -= dx[d]; c -= dy[d]
        if board[r][c] == 1:
            break

ans = 0
for i in range(N):
    for j in range(M):
        ans += visited[i][j]
print(ans)