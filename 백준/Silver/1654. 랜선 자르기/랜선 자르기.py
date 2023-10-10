import sys

K, N = map(int, sys.stdin.readline()[:-1].split())
LAN = [int(sys.stdin.readline()[:-1]) for k in range(K)]; LAN.sort()

left, right = 1, max(LAN)
while left <= right:
    mid = (left+right)//2

    cnt = 0
    for L in LAN:
        cnt += L // mid

    if cnt >= N: left = mid+1
    else: right = mid-1
print(right)