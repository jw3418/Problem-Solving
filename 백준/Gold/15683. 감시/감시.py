import sys
import copy

# 상 우 하 좌 순서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
modes = [[],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]]

def dfs(depth, Room):
    global min_result
    if depth == len(cctv):
        local_min_result = 0
        for i in range(N):
            for j in range(M):
                if Room[i][j] == 0:
                    local_min_result += 1
        min_result = min(min_result, local_min_result)
        return
    room = copy.deepcopy(Room)
    cctv_type, x, y = cctv[depth]
    for mode in modes[cctv_type]: #cctv의 모든 방향을 순회하며 backtracking 진행
        for idx in mode:
            nx = x; ny = y
            while True:
                nx += dx[idx]; ny += dy[idx]
                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    break
                if room[nx][ny] == 6:
                    break
                elif room[nx][ny] == 0:
                    room[nx][ny] = -1
        dfs(depth+1, room)
        room = copy.deepcopy(Room)

N, M = map(int, sys.stdin.readline()[:-1].split())
Room = []; cctv = []
for _ in range(N):
    tmp = list(map(int, sys.stdin.readline()[:-1].split()))
    Room.append(tmp)
    for i in range(M):
        if tmp[i] in [1, 2, 3, 4, 5]:
            cctv.append([tmp[i], _, i])

min_result = int(1e9)
dfs(0, Room)
print(min_result)