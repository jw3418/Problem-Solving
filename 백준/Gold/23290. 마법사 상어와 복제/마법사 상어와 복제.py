import sys
import copy
import heapq

dx = (0, -1, -1, -1, 0, 1, 1, 1)
dy = (-1, -1, 0, 1, 1, 1, 0, -1)
sdx = (-1, 0, 1, 0) #상좌하우 순서
sdy = (0, -1, 0, 1) #상좌하우 순서

def dfs(sx, sy, depth_path, fish_cnt, visit):
    if len(depth_path) >= 3:
        heapq.heappush(heap, [-fish_cnt, int(depth_path)])
        return

    for i in range(4):
        nsx = sx + sdx[i]; nsy = sy + sdy[i]
        if 0 <= nsx < 4 and 0 <= nsy < 4:
            if (nsx, nsy) not in visit:
                visit.append((nsx, nsy))
                dfs(nsx, nsy, depth_path+str(i+1), fish_cnt+len(board[nsx][nsy]), visit)
                visit.pop()
            else:
                dfs(nsx, nsy, depth_path+str(i+1), fish_cnt, visit)


M, S = map(int, sys.stdin.readline()[:-1].split())
board = [[[] for _ in range(4)] for _ in range(4)]
for m in range(M):
    fx, fy, d = map(int, sys.stdin.readline().strip().split()); fx-=1; fy-=1; d-=1
    if board[fx][fy]: board[fx][fy].append(d)
    else: board[fx][fy] = [d]
sx, sy = map(int, sys.stdin.readline().strip().split()); sx-=1; sy-=1
smell = dict()

for s in range(S):
    ##### 1. 복제 마법 시전
    backup_board = copy.deepcopy(board)

    ##### 2. 물고기 한 칸 이동
    tmp_board = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while board[x][y]:
                d = board[x][y].pop()
                for i in range(d, d-8, -1):
                    i %= 8
                    nx, ny = x+dx[i], y+dy[i]
                    if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != (sx, sy) and (nx, ny) not in smell:
                        tmp_board[nx][ny].append(i)
                        break
                else: tmp_board[x][y].append(d)
    board = copy.deepcopy(tmp_board)

    ##### 3. 상어 연속 3 칸 이동
    heap = []
    dfs(sx, sy, "", 0, []) #simulation 돌리기

    # 정한 경로로 상어 이동
    path = list(map(int, list(str(heap[0][1]))))
    for p in path:
        p-=1; sx += sdx[p]; sy += sdy[p]
        if board[sx][sy]: smell[(sx, sy)] = 2; board[sx][sy] = []

    ##### 4. 냄새 없애기
    removed_key = []
    for coor, s_cnt in smell.items():
        smell[coor] -= 1
        if s_cnt <= 0: removed_key.append(coor)
    for rk in removed_key: del smell[rk]

    ##### 5. 복제 마법 완료
    for i in range(4):
        for j in range(4):
            if len(backup_board[i][j]) > 0:
                tmp = backup_board[i][j]
                for f in range(len(tmp)):
                    if board[i][j]: board[i][j].append(tmp[f])
                    else: board[i][j] = [tmp[f]]

answer = 0
for i in range(4):
    for j in range(4):
        if board[i][j]: answer += len(board[i][j])
print(answer)