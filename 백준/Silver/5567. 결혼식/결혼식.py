import sys
from collections import deque
input = sys.stdin.readline

N = int(input()); M = int(input())
adj = [[] for n in range(N)]
for m in range(M):
    a, b = map(int, input().split()); a-=1; b-=1
    adj[a].append(b)
    adj[b].append(a)

queue = deque([]); queue.append((0, 0))
visit = [False]*N; visit[0] = True
ans = 0
while queue:
    cur, cnt = queue.popleft()
    if cnt < 2:
        for nex in adj[cur]:
            if not visit[nex]:
                ans += 1
                visit[nex] = True
                queue.append((nex, cnt+1))
print(ans)