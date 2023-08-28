import sys
from collections import deque

def cmd_1(): #상하반전
	global status_updown; global status_leftright; global status_rotate
	if status_rotate % 2: #배열이 90도 회전된 상태면 origin_arr 기준으로 봤을 때, 상하반전이 좌우반전이 되고 좌우반전이 상하반전이 됨
		status_leftright = not status_leftright
	else:
		status_updown = not status_updown

	mini_arr[0], mini_arr[1] = mini_arr[1], mini_arr[0]

def cmd_2(): #좌우반전
	global status_updown; global status_leftright; global status_rotate
	if status_rotate % 2: #배열이 90도 회전된 상태면 origin_arr 기준으로 봤을 때, 상하반전이 좌우반전이 되고 좌우반전이 상하반전이 됨
		status_updown = not status_updown
	else:
		status_leftright = not status_leftright

	mini_arr[0][1], mini_arr[0][0] = mini_arr[0][0], mini_arr[0][1]
	mini_arr[1][1], mini_arr[1][0] = mini_arr[1][0], mini_arr[1][1]

def cmd_3(): #오른쪽으로 90도 회전
	global status_rotate
	status_rotate = (status_rotate + 1) % 4
	cmd_5()

def cmd_4(): #왼족으로 90도 회전
	global status_rotate
	status_rotate = (status_rotate - 1) % 4 # -1 % 4 = 3임
	cmd_6()

def cmd_5(): #1->2, 2->4, 3->1, 4->3
	global mini_arr
	tmp_mini_arr = [[0, 0], [0, 0]]
	tmp_mini_arr[0][0] = mini_arr[1][0]
	tmp_mini_arr[0][1] = mini_arr[0][0]
	tmp_mini_arr[1][0] = mini_arr[1][1]
	tmp_mini_arr[1][1] = mini_arr[0][1]
	mini_arr = tmp_mini_arr

def cmd_6(): #1->3, 2->1, 3->4, 4->2
	global mini_arr
	tmp_mini_arr = [[0, 0], [0, 0]]
	tmp_mini_arr[0][0] = mini_arr[0][1]
	tmp_mini_arr[0][1] = mini_arr[1][1]
	tmp_mini_arr[1][0] = mini_arr[0][0]
	tmp_mini_arr[1][1] = mini_arr[1][0]
	mini_arr = tmp_mini_arr

def rotation(src_arr): #mini_arr를 회전
	dest_arr = [[0 for _ in range(len(src_arr))] for __ in range(len(src_arr[0]))] #회전하면 행개수와 열개수가 swap됨
	for i in range(len(src_arr[0])):
		for j in range(len(src_arr)):
			dest_arr[i][j] = src_arr[len(src_arr) - j - 1][i]
	return dest_arr


N, M, R = map(int, sys.stdin.readline()[:-1].split()) #N, M은 짝수/ N은 행개수, M은 열개수
arr = []
for n in range(N):
	arr.append(list(sys.stdin.readline()[:-1].split()))
cmds = list(map(int, sys.stdin.readline()[:-1].split()))

#기존 arr를 1, 2, 3, 4 구간으로 나누어 origin_arr에 할당
origin_arr = []
one = arr[:N//2]; two = arr[:N//2]; three = arr[N//2:]; four = arr[N//2:]
for i in range(N//2):
	two[i] = deque(two[i]); four[i] = deque(four[i])
	for _ in range(M//2):
		one[i].pop(); two[i].popleft(); three[i].pop(); four[i].popleft()
	two[i] = list(two[i]); four[i] = list(four[i])
origin_arr.append(one); origin_arr.append(two); origin_arr.append(three); origin_arr.append(four)

mini_arr = [[0, 1], [2, 3]] #origin_arr를 mini_arr로 표현
status_updown = False; status_leftright = False; status_rotate = 0 #각 origin_arr의 반전, 회전 상태를 나타냄
for cmd in cmds:
	if cmd == 1:
		cmd_1()
	elif cmd == 2:
		cmd_2()
	elif cmd == 3:
		cmd_3()
	elif cmd == 4:
		cmd_4()
	elif cmd == 5:
		cmd_5()
	elif cmd == 6:
		cmd_6()

if status_updown: #각 origin_arr별 상하반전 상태 적용
	for i in range(4):
		origin_arr[i].reverse()

if status_leftright: #각 origin_arr별 좌우반전 상태 적용
	for i in range(4):
		for j in range(len(origin_arr[i])):
			origin_arr[i][j].reverse()

for _ in range(status_rotate): #각 origin_arr별 회전 상태 적용
	for i in range(4):
		origin_arr[i] = rotation(origin_arr[i])

final_arr = []
final_arr.extend(origin_arr[mini_arr[0][0]])
final_arr.extend(origin_arr[mini_arr[1][0]])
for i in range(len(final_arr) // 2):
	final_arr[i].extend(origin_arr[mini_arr[0][1]][i])
	final_arr[i + len(final_arr) // 2].extend(origin_arr[mini_arr[1][1]][i])

for i in range(len(final_arr)):
	print(" ".join(final_arr[i]))