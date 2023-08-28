import sys
from collections import deque
sys.setrecursionlimit(10**9)

def dfs(start, weight):
	for element in adjacent[start]:
		if visit[element[0]] == -1:
			visit[element[0]] = weight + element[1]
			dfs(element[0], visit[element[0]])

n = int(input())
adjacent = [[] for _ in range(n+1)]
for _ in range(n-1):
	parent, child, weight = map(int, sys.stdin.readline()[:-1].split())
	adjacent[parent].append([child, weight])
	adjacent[child].append([parent, weight])

visit = [-1] * (n+1)
visit[1] = 0
dfs(1, 0) # 1번 노드에서 가장 먼 곳을 찾음

farest = visit.index(max(visit))
visit = [-1] * (n+1)
visit[farest] = 0
dfs(farest, 0) # 가장 먼 노드에 대해 가장 먼 노드를 찾음

print(max(visit))