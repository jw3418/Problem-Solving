import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque([]); queue.append((N, 0))
visit = [[-1]*2 for _ in range(500001)]; visit[N][0] = 0
while queue:
    cur_n, cnt = queue.popleft()
    if 0 <= (cur_n + 1) <= 500000 and visit[cur_n + 1][(cnt + 1) % 2] == -1:
        queue.append((cur_n + 1, cnt + 1))
        visit[cur_n + 1][(cnt + 1) % 2] = cnt + 1
    if 0 <= (cur_n - 1) <= 500000 and visit[cur_n - 1][(cnt + 1) % 2] == -1:
        queue.append((cur_n - 1, cnt + 1))
        visit[cur_n - 1][(cnt + 1) % 2] = cnt + 1  
    if 0 <= (cur_n * 2) <= 500000 and visit[cur_n * 2][(cnt + 1) % 2] == -1:
        queue.append((cur_n * 2, cnt + 1))
        visit[cur_n * 2][(cnt + 1) % 2] = cnt + 1

nex_k = K
for i in range(500001):
    nex_k += i
    if nex_k <= 500000:
        if visit[nex_k][i%2] <= i: print(i); exit()
    else: break
print(-1)