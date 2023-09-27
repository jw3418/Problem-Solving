import sys

N, S = map(int, sys.stdin.readline()[:-1].split())
nums = list(map(int, sys.stdin.readline()[:-1].split()))

left, right = 0, 0 # 투 포인터
s = 0
length = int(10e9) # 가장 작은 길이

while True:
    if s >= S:
        length = min(length, right - left); s -= nums[left]
        left += 1
    elif right == N: break
    else:
        s += nums[right]
        right += 1

if length == int(10e9): print(0)
else: print(length)