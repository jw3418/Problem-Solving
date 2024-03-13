import sys
from collections import deque
input = sys.stdin.readline

T = int(input().strip())
for t in range(T):
    N, K = map(int, input().strip().split())
    Time = [0]; Time.extend(list(map(int, input().strip().split())))

    graph = [[] for n in range(N+1)]
    indegree = [0]*(N+1)
    dp = [0]*(N+1)

    for k in range(K):
        x, y = map(int, input().strip().split())
        graph[x].append(y)
        indegree[y] += 1

    W = int(input().strip())

    queue = deque([])
    for n in range(1, N+1):
        if indegree[n] == 0:
            queue.append(n)
            dp[n]=Time[n]
    
    while queue:
        cur = queue.popleft()

        for nex in graph[cur]:
            indegree[nex] -= 1
            dp[nex] = max(dp[nex], dp[cur]+Time[nex])
            if indegree[nex] == 0: queue.append(nex)

    print(dp[W])