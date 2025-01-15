import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split()); M = len(str(N))

queue = deque([]); queue.append((N, 0))
visit = set(); visit.add((N, 0))
max_ = 0
while queue:
    n, k = queue.popleft()
    if k == K:
        max_ = max(max_, n)
    else:
        n = list(str(n))
        for i in range(M-1):
            for j in range(i+1, M):
                if i == 0 and n[j] == '0': continue
                n[i], n[j] = n[j], n[i]
                nn = int("".join(map(str, n)))
                if (nn, k+1) not in visit:
                    queue.append((nn, k+1))
                    visit.add((nn, k+1))
                n[i], n[j] = n[j], n[i]
if max_ == 0: print(-1)
else: print(max_)