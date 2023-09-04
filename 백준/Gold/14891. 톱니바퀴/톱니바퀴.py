import sys
from collections import deque

def left(gear_idx, direction):
	global Gears
	if gear_idx < 0:
		return
	if Gears[gear_idx][2] == Gears[gear_idx+1][6]:
		return
	
	if Gears[gear_idx][2] != Gears[gear_idx+1][6]:
		left(gear_idx-1, -direction) #왼쪽 gear 더 조사
		Gears[gear_idx].rotate(direction)

def right(gear_idx, direction):
	global Gears
	if gear_idx >= 4:
		return
	if Gears[gear_idx][6] == Gears[gear_idx-1][2]:
		return
	
	if Gears[gear_idx][6] != Gears[gear_idx-1][2]:
		right(gear_idx+1, -direction) #오른쪽 gear 더 조사
		Gears[gear_idx].rotate(direction)

Gears = []
for _ in range(4):
	Gears.append(deque(list(map(int, sys.stdin.readline()[:-1]))))
K = int(input())
rotation = []
for _ in range(K):
	rotation.append(list(map(int, sys.stdin.readline()[:-1].split())))

for k in range(K): #각 회전 수행
	gear_idx = rotation[k][0] - 1
	left(gear_idx - 1, -rotation[k][1]) #왼쪽 탐색
	right(gear_idx + 1, -rotation[k][1]) #오른쪽 탐색
	Gears[gear_idx].rotate(rotation[k][1]) #기존 gear 회전
	# 탐색 완료한 후 기존 gear를 회전시켜야함! (탐색하는 과정에서 Gears의 상태가 변하면 안됨)
#score 계산
score = 0; weight = 0
for i in range(4):
	weight = 2**i
	if Gears[i][0] == 1: score += weight
print(score)