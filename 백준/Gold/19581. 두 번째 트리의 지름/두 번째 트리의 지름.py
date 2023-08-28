import sys
from collections import deque

def bfs(curr, weight):
    queue = deque([])
    queue.append((curr, weight))
    visit = [-1] * (N+1)
    visit[curr] = 0

    while queue:
        curr, weight = queue.popleft()
        for nnode, nweight in graph[curr]:
            if visit[nnode] == -1:
                visit[nnode] = weight + nweight
                queue.append((nnode, visit[nnode]))

    return visit.index(max(visit))

def solution_bfs(curr, weight, ban_node):
    queue = deque([])
    queue.append((curr, weight))
    visit = [-1] * (N+1)
    visit[curr] = 0

    while queue:
        curr, weight = queue.popleft()
        for nnode, nweight in graph[curr]:
            if nnode != ban_node:
                if visit[nnode] == -1:
                    visit[nnode] = weight + nweight
                    queue.append((nnode, visit[nnode]))

    return max(visit)


N = int(sys.stdin.readline()[:-1])
graph = dict()
for n in range(N-1):
    curr, next, weight = map(int, sys.stdin.readline()[:-1].split())
    if curr in graph:
        graph[curr].append((next, weight))
    elif curr not in graph:
        graph[curr] = [(next, weight)]
    if next in graph:
        graph[next].append((curr, weight))
    elif next not in graph:
        graph[next] = [(curr, weight)]

farest_node_1 = bfs(1, 0)
farest_node_2 = bfs(farest_node_1, 0)

# farest_node_2를 제거한 후에 farest_node_1에서 가장 먼 노드 찾기
candidate1 = solution_bfs(farest_node_1, 0, farest_node_2)

# farest_node_1을 제거한 후에 farest_node_2에서 가장 먼 노드 찾기
candidate2 = solution_bfs(farest_node_2, 0, farest_node_1)

print(max(candidate1, candidate2))