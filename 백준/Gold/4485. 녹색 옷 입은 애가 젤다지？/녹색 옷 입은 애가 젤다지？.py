import sys
import heapq

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def dijkstra():
    heap = []; heapq.heappush(heap, (graph[0][0], 0, 0))
    costs[0][0] = 0

    while heap:
        cost, x, y = heapq.heappop(heap)

        if (x, y) == (N-1, N-1):
            print("Problem " + str(cnt) + ": " + str(cost)); break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                ncost = cost + graph[nx][ny]
                if costs[nx][ny] > ncost:
                    costs[nx][ny] = ncost
                    heapq.heappush(heap, (ncost, nx, ny))


cnt = 0
while True:
    cnt += 1; N = int(sys.stdin.readline()[:-1])
    if N == 0: break

    graph = [list(map(int, sys.stdin.readline()[:-1].split())) for n in range(N)]
    costs = [[int(10e9)]*N for n in range(N)]

    dijkstra()