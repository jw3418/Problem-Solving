import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def enable_fish(visit):
	global shark_size

	min_distance = 1e9
	x, y = 0, 0
	for i in range(N):
		for j in range(N):
			if visit[i][j] != -1 and 1 <= Map[i][j] < shark_size:
				if visit[i][j] < min_distance:
					min_distance = visit[i][j]
					x, y = i, j

	if min_distance == 1e9: # 먹을 물고기가 없는 경우
		return -1
	else:
		return x, y, min_distance

def move():
	global shark_position_x; global shark_position_y
	global shark_size

	queue = deque([])
	queue.append([shark_position_x, shark_position_y])

	visit = [[-1] * N for n in range(N)]
	visit[shark_position_x][shark_position_y] = 0

	while queue:
		tmp = queue.popleft(); x = tmp[0]; y = tmp[1]

		for i in range(4):
			nx = x + dx[i]; ny = y + dy[i]
			if nx < 0 or ny < 0 or nx >= N or ny >= N:
				continue
			
			if visit[nx][ny] == -1:
				if Map[nx][ny] <= shark_size:
					visit[nx][ny] = visit[x][y] + 1
					queue.append([nx, ny])
	
	return visit

				
N = int(input())
Map = []
for _ in range(N):
	Map.append(list(map(int, sys.stdin.readline()[:-1].split())))

####################
shark_position_x = -1; shark_position_y = -1 # 상어의 현재 위치
for i in range(N):
	for j in range(N):
		if Map[i][j] == 9:
			shark_position_x = i; shark_position_y = j
			Map[shark_position_x][shark_position_y] = 0
			break
shark_size = 2 # 상어의 현재 크기
shark_current_eat = 0 # 상어가 현재 크기에서 먹은 물고기의 개수
answer = 0 # 상어가 지금까지 이동한 거리
####################

while True:
	result = enable_fish(move())
	if result == -1:
		print(answer)
		break
	else:
		shark_position_x = result[0]; shark_position_y = result[1]
		answer += result[2]
		Map[shark_position_x][shark_position_y] = 0
		shark_current_eat += 1
		if shark_current_eat == shark_size:
			shark_size += 1
			shark_current_eat = 0