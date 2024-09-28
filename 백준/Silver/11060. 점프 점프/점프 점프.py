import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

queue = deque([]); queue.append((0, 0))
visit = [False]*N; visit[0] = True
li = []
while queue:
    cur, cnt = queue.popleft()
    if cur == N-1: li.append(cnt)
    else:
        for step in range(1, A[cur]+1):
            nex = cur + step
            if nex < N and not visit[nex]:
                visit[nex] = True
                queue.append((nex, cnt+1))
if not li: print(-1)
else: print(min(li))