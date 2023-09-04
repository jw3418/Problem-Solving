import sys
from collections import deque

di = [0, 0, -1, 1, 0, 0]
dj = [-1, 1, 0, 0, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

def bfs():
	queue = deque([])
	for _ in range(len(start)):
		queue.append(start[_])

	while queue:
		h, i, j = map(int, queue.popleft())

		for _ in range(6):
			ni = i + di[_]; nj = j + dj[_]; nh = h + dh[_]
			if ni < 0 or nj < 0 or nh < 0 or ni >= N or nj >= M or nh >= H:
				continue
			if box[nh][ni][nj] == 0:
				box[nh][ni][nj] = box[h][i][j] + 1
				queue.append([nh, ni, nj])

M, N, H = map(int, sys.stdin.readline().split())

box = []
for h in range(H):
	tmp = []
	for n in range(N):
		tmp.append(list(map(int, sys.stdin.readline().split())))
	box.append(tmp)

start = []
for h in range(H):
	for i in range(N):
		for j in range(M):
			if box[h][i][j] == 1:
				start.append([h, i, j])

bfs(); date = 0
for h in range(H):
	for i in range(N):
		for j in range(M):
			if box[h][i][j] == 0:
				print(-1); exit()
		date = max(max(box[h][i]), date)
print(date-1)