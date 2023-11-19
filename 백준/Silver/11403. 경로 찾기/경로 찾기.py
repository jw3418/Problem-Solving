from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*N for _ in range(N)]

for i in range(N):
    queue = deque(); queue.append(i)
    check = [False for _ in range(N)]

    while queue:
        cur = queue.popleft()
        for j in range(N):
            if not check[j] and graph[cur][j] == 1:
                queue.append(j)
                check[j] = True; visit[i][j] = 1

for _ in visit: print(*_)