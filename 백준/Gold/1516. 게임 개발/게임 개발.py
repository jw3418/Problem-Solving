import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())

graph = [[] for n in range(N+1)]
indegree = [0] * (N+1)
cost = [0] * (N+1)

for n in range(1, N+1):
    tmp = list(map(int, input().strip().split()))
    cost[n] = tmp[0]
    for i in range(1, len(tmp)-1):
        graph[tmp[i]].append(n); indegree[n] += 1

queue = deque([])
for n in range(1, N+1):
    if indegree[n] == 0: queue.append(n)

result = [0] * (N+1)
while queue:
    cur = queue.popleft()
    result[cur] += cost[cur]

    for nex in graph[cur]:
        indegree[nex] -= 1
        result[nex] = max(result[nex], result[cur]) #선수 건물 중 가장 많이 걸리는 시간으로 갱신해야함
        if indegree[nex] == 0: queue.append(nex)
print("\n".join(map(str, result[1:])))