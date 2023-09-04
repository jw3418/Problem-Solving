import sys

# 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다. 
N = int(input())
student = dict()
for _ in range(N**2):
	tmp = list(map(int, sys.stdin.readline()[:-1].split()))
	student[tmp[0]] = set(tmp[1:])

dx = [0, 0, -1, 1]; dy = [-1, 1, 0, 0]
classroom = [[0 for _ in range(N)] for __ in range(N)]
for key, value in student.items():
	candidate = []
	for i in range(N-1, -1, -1):
		for j in range(N-1, -1, -1):
			if classroom[i][j] == 0:
				like_cnt = 0; empty_cnt = 0
				for s in range(4):
					nx = i + dx[s]; ny = j + dy[s]
					if 0 <= nx < N and 0 <= ny < N:
						if classroom[nx][ny] in value:
							like_cnt += 1
						if classroom[nx][ny] == 0:
							empty_cnt += 1
				candidate.append([like_cnt, empty_cnt, i, j])
	candidate.sort(key = lambda x:(-x[0], -x[1], x[2], x[3]))
	classroom[candidate[0][2]][candidate[0][3]] = key

total_score = 0
for i in range(N):
	for j in range(N):
		score = 0
		for s in range(4):
			nx = i + dx[s]; ny = j + dy[s]
			if 0 <= nx < N and 0 <= ny < N:
				if classroom[nx][ny] in student[classroom[i][j]]:
					score += 1
		if score != 0:
			total_score += 10 ** (score - 1)
print(total_score)