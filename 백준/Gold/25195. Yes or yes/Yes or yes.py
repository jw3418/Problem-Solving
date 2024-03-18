import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().strip().split())
graph = [[] for n in range(N+1)]
for m in range(M):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
S = int(input())
sss = list(map(int, input().strip().split()))
sss = set(sss)
if 1 in sss:
    print("Yes"); exit()

queue = deque([]); queue.append(1)
visit = [False]*(N+1); visit[1] = True
while queue:
    cur = queue.popleft()
    if not graph[cur]:
        print("yes"); exit()
    for nex in graph[cur]:
        if not visit[nex] and nex not in sss:
            queue.append(nex)
            visit[nex] = True
print("Yes")