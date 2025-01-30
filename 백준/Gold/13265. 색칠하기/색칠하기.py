import sys
from collections import deque
input = sys.stdin.readline


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    graph = dict()
    for m in range(M):
        x, y = map(int, input().split())
        if x in graph: graph[x].append(y)
        else: graph[x] = [y]
        if y in graph: graph[y].append(x)
        else: graph[y] = [x]
    
    visit = [-1]*(N+1)
    flag = True
    for i in range(1, N+1):
        if visit[i] == -1:
            queue = deque([]); queue.append(i)
            visit[i] = 0
            while queue:
                cur = queue.popleft()
                if cur in graph:
                    for nex in graph[cur]:
                        if visit[nex] == -1:
                            visit[nex] = visit[cur] + 1
                            queue.append(nex)
                        elif visit[nex]%2 == visit[cur]%2:
                            flag = False; break
                if not flag: break
        if not flag: break
    if flag: print("possible")
    else: print("impossible")

    # print(visit)