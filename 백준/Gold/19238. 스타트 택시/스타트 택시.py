import sys
from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def find_passenger(t_x, t_y):
    global energy
    global taxi_x, taxi_y
    
    if (t_x, t_y) in src:
        taxi_x = t_x; taxi_y = t_y
        return True

    queue = deque([]); queue.append((t_x, t_y))
    visit = [[-1] * N for _ in range(N)]
    visit[t_x][t_y] += 1
    passenger = []

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] != 1 and visit[nx][ny] == -1:
                    if (nx, ny) in src:
                        visit[nx][ny] = visit[x][y] + 1
                        passenger.append((visit[nx][ny], nx, ny))
                    else:
                        visit[nx][ny] = visit[x][y] + 1
                        queue.append((nx, ny))
    if not passenger:
        return False
    
    passenger.sort()
    passenger = passenger[0]
    if passenger[0] <= energy:
        energy -= passenger[0]
        taxi_x = passenger[1]; taxi_y = passenger[2]
        return True
    else:
        return False

def goto_dest(s_x, s_y, d_x, d_y): #한 승객의 도착지가 다른 승객의 출발지인 경우가 있을 수 있음
    global energy
    global taxi_x, taxi_y

    queue = deque([]); queue.append((s_x, s_y))
    visit = [[-1] * N for _ in range(N)]
    visit[s_x][s_y] += 1
    distance = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] != 1 and visit[nx][ny] == -1:
                    if nx == d_x and ny == d_y:
                        visit[nx][ny] = visit[x][y] + 1
                        distance = visit[nx][ny]
                        if distance <= energy:
                            energy += distance
                            taxi_x = nx; taxi_y = ny
                            return True
                        else:
                            return False
                    else:
                        visit[nx][ny] = visit[x][y] + 1
                        queue.append((nx, ny))
    return False



N, M, energy = map(int, sys.stdin.readline()[:-1].split())
board = []
for n in range(N):
    board.append(list(map(int, sys.stdin.readline()[:-1].split())))

taxi_x, taxi_y = map(int, sys.stdin.readline()[:-1].split())
taxi_x -= 1; taxi_y -= 1
src = set(); dest = set(); src_dest = []
for m in range(M):
    s_x, s_y, d_x, d_y = map(int, sys.stdin.readline()[:-1].split())
    s_x -= 1; s_y -= 1; d_x -= 1; d_y -= 1
    src.add((s_x, s_y)); dest.add((d_x, d_y))
    src_dest.append((s_x, s_y, d_x, d_y)) 

turn = 0
while True:
    ##### 가까운 승객 찾기
    if not find_passenger(taxi_x, taxi_y):
        print(-1)
        exit()
    s_x = taxi_x; s_y = taxi_y
    ##### 승객 데려다주기
    d_x = -1; d_y = -1
    for i in range(len(src_dest)):
        if src_dest[i][0] == s_x and src_dest[i][1] == s_y:
            d_x = src_dest[i][2]; d_y = src_dest[i][3]
    if not goto_dest(s_x, s_y, d_x, d_y):
        print(-1)
        exit()

    ##### 승객의 출발지와 도착지 갱신
    # src, dest, src_dest에서 없애주기
    src.discard((s_x, s_y))
    dest.discard((d_x, d_y))
    src_dest.remove((s_x, s_y, d_x, d_y))

    turn += 1

    ##### 다 데려다 준 경우 (더 이상 승객이 없는 경우) 종료
    if turn == M:
        if len(src_dest) != 0:
            print(-1)
            exit()
        else:
            break

print(energy)