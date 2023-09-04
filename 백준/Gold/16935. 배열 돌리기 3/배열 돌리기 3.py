import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline()[:-1].split()) #N, M은 짝수/ N은 행개수, M은 열개수
arr = []
for n in range(N):
	arr.append(list(sys.stdin.readline()[:-1].split()))
cmds = list(map(int, sys.stdin.readline()[:-1].split()))

for cmd in cmds:
	if cmd == 1: #상하반전
		arr = arr[::-1]
	elif cmd == 2: #좌우반전
		for i in range(N):
			arr[i] = arr[i][::-1]
	elif cmd == 3: #오른쪽으로 90도 회전
		result = []
		for m in range(M):
			tmp = []
			for n in range(N-1, -1, -1):
				tmp.append(arr[n][m])
			result.append(tmp)
		arr = result
		tmp = N; N = M; M = tmp
	elif cmd == 4: #왼쪽으로 90도 회전
		result = []
		for m in range(M-1, -1, -1):
			tmp = []
			for n in range(N):
				tmp.append(arr[n][m])
			result.append(tmp)
		arr = result
		tmp = N; N = M; M = tmp
	elif cmd == 5: #1->2, 2->3, 3->4, 4->1
		one = arr[:N//2]; two = arr[:N//2]; three = arr[N//2:]; four = arr[N//2:]
		for i in range(N//2):
			two[i] = deque(two[i]); three[i] = deque(three[i])
			for _ in range(M//2):
				one[i].pop(); two[i].popleft(); three[i].popleft(); four[i].pop()
			two[i] = list(two[i]); three[i] = list(three[i])
		for i in range(N):
			if i < N//2: #1에 4넣고, 2에 1넣기
				tmp = four[i]; tmp.extend(one[i])
				arr[i] = tmp
			else: #4에 3넣고, 3에 2넣기
				tmp = three[i-N//2]; tmp.extend(two[i-N//2])
				arr[i] = tmp
	elif cmd == 6: #1->4, 4->3, 3->2, 2->1
		one = arr[:N//2]; two = arr[:N//2]; three = arr[N//2:]; four = arr[N//2:]
		for i in range(N//2):
			two[i] = deque(two[i]); three[i] = deque(three[i])
			for _ in range(M//2):
				one[i].pop(); two[i].popleft(); three[i].popleft(); four[i].pop()
			two[i] = list(two[i]); three[i] = list(three[i])
		for i in range(N):
			if i < N//2: #1에 2넣고, 2에 3넣기
				tmp = two[i]; tmp.extend(three[i])
				arr[i] = tmp
			else: #4에 1넣고, 3에 4넣기
				tmp = one[i-N//2]; tmp.extend(four[i-N//2])
				arr[i] = tmp

for i in range(len(arr)):
	print(" ".join(arr[i]))