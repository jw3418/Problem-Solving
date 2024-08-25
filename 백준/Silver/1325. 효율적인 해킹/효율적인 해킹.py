import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for n in range(N)]
for m in range(M):
    A, B = map(int, input().split()); A-=1; B-=1
    graph[B].append(A)

def bfs(cur):
    cnt = 1
    queue = deque([]); queue.append(cur)
    visit = [False]*N; visit[cur] = True
    while queue:
        cur = queue.popleft()
        for nex in graph[cur]:
            if not visit[nex]:
                visit[nex] = True
                queue.append(nex)
                cnt += 1
    return cnt

result = []; max_ = 0
for n in range(N):
    cnt = bfs(n)
    max_ = max(max_, cnt)
    result.append((n+1, cnt))

ans = []
for n, cnt in result:
    if cnt == max_: ans.append(n)
ans.sort(); print(" ".join(map(str, ans)))