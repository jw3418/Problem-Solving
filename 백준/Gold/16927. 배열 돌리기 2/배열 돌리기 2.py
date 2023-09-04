import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline()[:-1].split())
arr = []
for n in range(N):
	arr.append(list(sys.stdin.readline()[:-1].split()))

answer = [[0] * M for n in range(N)]
for i in range(min(N, M) // 2): #껍질의 개수만큼 순회 (N = 5, M = 4라면 4 // 2인 2가 껍질의 개수가 됨)
	queue = deque([]) #껍질별로 위쪽, 오른쪽, 아래쪽, 왼쪽 순서(시계방향)로 넣어줄거임
	queue.extend(arr[i][i:M - i]) #위쪽
	queue.extend([row[M - i - 1] for row in arr[i + 1: N - i - 1]]) #오른쪽
	queue.extend(arr[N - i - 1][i:M - i][::-1]) #아래쪽
	queue.extend([row[i] for row in arr[i + 1:N - i - 1]][::-1]) #왼쪽

	queue.rotate(-R) #반시계방향으로 R만큼 회전

	#answer 2차원 리스트에 회전한 값(회전한 껍질) 넣기
	for j in range(i, M - i): #위쪽(i, 4-i)
		answer[i][j] = queue.popleft()
	for j in range(i + 1, N - i - 1): #오른쪽(i+1, 4-i)
		answer[j][M - i - 1] = queue.popleft()
	for j in range(M - i - 1, i - 1, -1): #아래쪽(3-i, i-1, -1)
		answer[N - i - 1][j] = queue.popleft()
	for j in range(N - i - 2, i, -1): #왼쪽(3-i, i, -1)
		answer[j][i] = queue.popleft()

for i in range(len(answer)):
	print(" ".join(answer[i]))