import sys
from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def search(x, y, number):
    queue = deque([]); queue.append((x, y))
    visit[x][y] = True
    will_removed = [(x, y)]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 1 <= nx < N+1:
                if 0 <= ny < M:
                    if disk[nx][ny] == number and not visit[nx][ny]:
                        queue.append((nx, ny))
                        visit[nx][ny] = True
                        will_removed.append((nx, ny))
                elif ny == -1:
                    ny = M-1
                    if disk[nx][ny] == number and not visit[nx][ny]:
                        queue.append((nx, ny))
                        visit[nx][ny] = True
                        will_removed.append((nx, ny))
                elif ny == M:
                    ny = 0
                    if disk[nx][ny] == number and not visit[nx][ny]:
                        queue.append((nx, ny))
                        visit[nx][ny] = True
                        will_removed.append((nx, ny))
    return will_removed

def disk_remove(will_removeds):
    for i in range(len(will_removeds)):
        for x, y in will_removeds[i]:
            disk[x][y] = 'x'

def get_total(disk):
    total = 0; count = 0
    for i in range(1, N+1):
        for j in range(M):
            if disk[i][j] != 'x':
                total += disk[i][j]
                count += 1
    return total, count


N, M, T = map(int, sys.stdin.readline()[:-1].split())
disk = [deque([])]
for n in range(N):
    disk.append(deque(list(map(int, sys.stdin.readline()[:-1].split()))))

for t in range(T):
    x, d, k = map(int, sys.stdin.readline()[:-1].split())

    ##### x의 배수인 원판 찾고 d방향으로 k칸 회전
    for i in range(1, N+1):
        if i % x == 0:
            if d == 0: disk[i].rotate(k)
            elif d == 1: disk[i].rotate((-1)*k)

    ##### 인접하면서 수가 같은 것들을 찾음 (0은 제외)
    will_removeds = []
    visit = [[False] * M for _ in range(N+1)]
    for x in range(1, N+1):
        for y in range(M):
            if disk[x][y] != 'x' and not visit[x][y]:
                tmp = search(x, y, disk[x][y])
                if len(tmp) > 1:
                    will_removeds.append(tmp)

    ##### 있다면 해당 수들을 지움
    if len(will_removeds) != 0:
        disk_remove(will_removeds)

    ##### 없다면 원판에 적힌 수의 평균을 구하고 +- 1 진행
    else:
        total, count = get_total(disk)
        if count == 0:
            break
        average = total / count
        for i in range(1, N+1):
            for j in range(M):
                if disk[i][j] != 'x':
                    if disk[i][j] > average:
                        disk[i][j] -= 1
                    elif disk[i][j] < average:
                        disk[i][j] += 1

result, count = get_total(disk)
print(result)