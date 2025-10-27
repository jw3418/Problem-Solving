import sys
from collections import deque
input = sys.stdin.readline

A, K = map(int, input().split())

queue = deque([]); queue.append((A, 0))
visited = set(); visited.add(A)
ans = -1
while queue:
    cur_a, depth = queue.popleft()
    if cur_a == K:
        ans = depth
        break
    for nex_a in (cur_a + 1, cur_a * 2):
        if nex_a <= K and nex_a not in visited:
            visited.add(nex_a)
            queue.append((nex_a, depth + 1))
print(ans)