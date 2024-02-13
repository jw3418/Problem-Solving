import sys
from collections import deque

N = int(sys.stdin.readline().strip())
adj = [[] for _ in range(N+1)]
while True:
    a, b = map(int, sys.stdin.readline().strip().split())
    if a==-1 and b==-1: break
    adj[a].append(b); adj[b].append(a)

score_min = 50; candi = []

for n in range(1, N+1):
    queue = deque([]); queue.append(n)
    visit = [-1] * (N+1); visit[n] = 0
    while queue:
        cur = queue.popleft()
        for nex in adj[cur]:
            if visit[nex] == -1:
                queue.append(nex)
                visit[nex] = visit[cur]+1
    score_tmp = max(visit)
    if score_tmp < score_min:
        score_min = score_tmp; candi = [n]
    elif score_tmp == score_min:
        candi.append(n)
print(score_min, len(candi)); print(" ".join(map(str, candi)))