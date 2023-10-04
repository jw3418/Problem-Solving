import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque([]); queue.append((src[0], src[1]))
    visit = [False for _ in range(N)] #편의점들

    while queue:
        x, y = queue.popleft()
        if abs(x - dest[0])+abs(y-dest[1]) <= 1000:
            print("happy"); return
        else:
            for i in range(N):
                if not visit[i]:
                    nx, ny = mid[i]
                    if abs(x-nx)+abs(y-ny) <= 1000:
                        queue.append((nx, ny))
                        visit[i] = True
    print("sad"); return


T = int(input()[:-1])
for t in range(T):
    N = int(input()[:-1])

    src = list(map(int, input()[:-1].split()))
    mid = []
    for n in range(N): mid.append(list(map(int, input()[:-1].split())))
    dest = list(map(int, input()[:-1].split()))
    bfs()