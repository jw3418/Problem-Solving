import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
S-=1; G-=1

visit = [False]*F
queue = deque([])
queue.append((S, 0))

ans = int(10e9)
while queue:
    cur, cnt = queue.popleft()
    if cur == G:
        ans = min(ans, cnt)
    else:
        if cur+U < F and not visit[cur+U]:
            queue.append((cur+U, cnt+1))
            visit[cur+U] = True
        if cur-D >= 0 and not visit[cur-D]:
            queue.append((cur-D, cnt+1))
            visit[cur-D] = True

if ans == int(10e9): print("use the stairs")
else: print(ans)