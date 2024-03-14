import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for n in range(N+1)]
indegree = [0]*(N+1)
time = [0]*(N+1)
dp = [0]*(N+1)
for n in range(1, N+1):
    tmp = list(map(int, input().strip().split()))
    time[n] = tmp[0]
    if tmp[1] != 0:
        for m in range(2, len(tmp)):
            indegree[n] += 1
            graph[tmp[m]].append(n)

queue = deque([])
for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)
        dp[i] = time[i]

while queue:
    cur = queue.popleft()
    for nex in graph[cur]:
        indegree[nex] -= 1
        dp[nex] = max(dp[nex], dp[cur]+time[nex])
        if indegree[nex] == 0:
            queue.append(nex)

print(max(dp))