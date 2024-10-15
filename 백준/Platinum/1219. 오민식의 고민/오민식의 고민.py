import sys
from collections import deque
input = sys.stdin.readline

N, A, B, M = map(int, input().split())
graph = []
for m in range(M):
    a, b, c = map(int, input().split())
    graph.append([a, b, -c])
costs = [-int(10e9) for n in range(N)]
money = list(map(int, input().split()))
for m in range(M): graph[m][2] = graph[m][2]+money[graph[m][1]]

def bfs(s, e): # 음수사이클 확인할 때 도착지점으로 갈 수 있는 지 추가로 확인해줘야함
    queue = deque([]); queue.append(s)
    visit = [False]*N; visit[s] = True
    while queue:
        cur = queue.popleft()
        if cur == e: return True
        for m in range(M):
            a, b, _ = graph[m]
            if cur == a:
                if not visit[b]:
                    queue.append(b)
                    visit[b] = True
    return False

def BellmanFord(s, e):
    costs[s] = money[s]

    for n in range(N-1):
        for m in range(M):
            cur, nex, ccost = graph[m]
            if costs[cur] != -int(10e9):
                if costs[nex] < costs[cur]+ccost:
                    costs[nex] = costs[cur]+ccost

    if costs[e] == -int(10e9): print("gg"); return

    for m in range(M): # N번째 돌았을 때 갱신된다면 Gee
        cur, nex, ccost = graph[m]
        if costs[cur] != -int(10e9):
            if costs[nex] < costs[cur]+ccost:
                if bfs(nex, e): print("Gee"); return
    
    print(costs[e]); return

BellmanFord(A, B)