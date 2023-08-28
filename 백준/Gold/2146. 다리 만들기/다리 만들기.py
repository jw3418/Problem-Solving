import sys
from collections import deque

dx = [0, 0, -1 ,1]
dy = [-1, 1, 0, 0]

def bfs_partition(start, color):
	queue = deque([])
	queue.append(start)
	
	while queue:
		x, y = queue.popleft()
		
		for i in range(4):
			nx = x + dx[i]; ny = y + dy[i]
			if 0 <= nx < N and 0 <= ny < N:
				if Map[nx][ny] != 0 and not visit[nx][ny]:
					Map[nx][ny] = color
					visit[nx][ny] = True
					queue.append([nx, ny])

def bfs_bridge(color):
	distance = [[-1] * N for _ in range(N)]

	queue = deque([])
	for i in range(N):
		for j in range(N):
			if Map[i][j] == color:
				distance[i][j] = 0
				queue.append([i, j])
	
	while queue:
		x, y = queue.popleft()

		for i in range(4):
			nx = x + dx[i]; ny = y + dy[i]
			if 0 <= nx < N and 0 <= ny < N:
				if Map[nx][ny] != 0 and Map[nx][ny] != color: #다른 섬에 도착 -> 이전 노드의 distance 값을 반환
					return distance[x][y]
				if Map[nx][ny] == 0 and distance[nx][ny] == -1:
					distance[nx][ny] = distance[x][y] + 1
					queue.append([nx, ny])



N = int(input())
Map = []
for _ in range(N):
	Map.append(list(map(int, sys.stdin.readline()[:-1].split())))

visit = [[False] * N for _ in range(N)]; color = 1
for i in range(N):
	for j in range(N):
		if Map[i][j] != 0 and not visit[i][j]:
			visit[i][j] = True; Map[i][j] = color
			bfs_partition([i, j], color)
			color += 1

global_min = 1e9
for i in range(1, color):
	local_min = bfs_bridge(i)
	global_min = min(local_min, global_min)
print(global_min)