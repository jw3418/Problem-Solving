import sys
from collections import deque

counter = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0} #주사위의 밑면에 해당하는 윗면 (index로 매칭)

N = int(input())
dice = []
for _ in range(N):
	dice.append(list(map(int, sys.stdin.readline()[:-1].split())))

global_max = 0
for i in range(6): #1번 주사위를 돌리는 경우 -> 6가지
	dice_max_sum = []
	tmp_dice = [1, 2, 3, 4, 5, 6]
	tmp_dice.remove(dice[0][i]) #1번 주사위의 아랫면 제거
	previous_high = dice[0][counter[i]] #이전 윗면 할당
	tmp_dice.remove(dice[0][counter[i]]) #1번 주사위의 윗면 제거
	dice_max_sum.append(max(tmp_dice))
	for j in range(1, N):
		tmp_dice = [1, 2, 3, 4, 5, 6]
		low_index = dice[j].index(previous_high)
		tmp_dice.remove(dice[j][low_index]) #j번 주사위의 아랫면 제거
		previous_high = dice[j][counter[low_index]] #이전 윗면 갱신
		tmp_dice.remove(dice[j][counter[low_index]]) #j번 주사위의 윗면 제거
		dice_max_sum.append(max(tmp_dice))
	
	local_max = sum(dice_max_sum)
	if local_max > global_max:
		global_max = local_max

print(global_max)