import sys
from collections import deque
sys.setrecursionlimit(10**9)

def dfs(start, weight):
	for element in adjacent[start]:
		if visit[element[0]] == -1:
			visit[element[0]] = weight + element[1]
			dfs(element[0], visit[element[0]])

V = int(input())
adjacent = [[] for _ in range(V+1)]
for _ in range(V):
	tmp = list(map(int, sys.stdin.readline()[:-1].split()))
	parent = tmp[0]
	for i in range(1, len(tmp)-1, 2):
		adjacent[parent].append([tmp[i], tmp[i+1]])


visit = [-1] * (V+1)
visit[1] = 0
dfs(1, 0) # 1번 노드에서 가장 먼 곳을 찾음

farest = visit.index(max(visit))
visit = [-1] * (V+1)
visit[farest] = 0
dfs(farest, 0) # 가장 먼 노드에 대해 가장 먼 노드를 찾음

print(max(visit))