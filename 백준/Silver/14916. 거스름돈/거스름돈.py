import sys

N = int(sys.stdin.readline().strip())

cnt = 0
while N > 0:
    if N % 5 == 0: cnt += N//5; break
    else: N -= 2; cnt += 1

if N < 0: print(-1)
else: print(cnt)