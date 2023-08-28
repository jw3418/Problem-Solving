import sys
from collections import deque
sys.setrecursionlimit(10**5)

def dfs(is_dfs):
	curr_node = is_dfs.popleft()
	visit[curr_node] = True
	if not is_dfs: #is_dfs의 모든 노드들을 출력한 경우 1 출력하고 종료
		print(1); exit(0)
	for i in range(len(adjacent[curr_node])): #curr_node에 연결되어 있는 자식 노드의 개수만큼 반복 -> 그래야 is_dfs의 원소가 단계에 맞게 popleft됨
		if not visit[is_dfs[0]] and is_dfs[0] in adjacent[curr_node]:
			dfs(is_dfs)
	return False

N = int(input())
adjacent = [[] for _ in range(N+1)]
for _ in range(N-1):
	t0, t1 = map(int, sys.stdin.readline()[:-1].split())
	adjacent[t0].append(t1)
	adjacent[t1].append(t0)
is_dfs = deque(list(map(int, sys.stdin.readline()[:-1].split())))

visit = [False] * (N+1)

if is_dfs[0] != 1:
	print(0); exit(0)
if not dfs(is_dfs):
	print(0)