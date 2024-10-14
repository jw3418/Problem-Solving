import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
tmp = list(map(int, input().split()))
queue = deque([])
for n in range(N): queue.append((n+1, tmp[n]))

ans = ""
while queue:
    idx, num = queue.popleft()
    ans += str(idx)+" "
    if num > 0:
        queue.rotate(-(num-1))
    else:
        queue.rotate(-num)
print(ans)