import sys
from collections import deque

H, W = map(int, input().split())
world = list(map(int, sys.stdin.readline()[:-1].split()))

total = 0
for i in range(1, W-1):
	left_max = max(world[:i]); right_max = max(world[i+1:])
	
	if world[i] < min(left_max, right_max):
		total += min(left_max, right_max) - world[i]

print(total)