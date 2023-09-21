import sys
from collections import deque

N, M = map(int, sys.stdin.readline()[:-1].split())
pos = list(map(int, sys.stdin.readline()[:-1].split()))
queue = deque([i for i in range(1, N+1)])

count = 0
for i in pos:
    while True:
        if queue[0] == i:
            queue.popleft(); break
        else:
            if queue.index(i) < len(queue)/2:
                while queue[0] != i:
                    queue.rotate(-1); count += 1
            else:
                while queue[0] != i:
                    queue.rotate(1); count += 1
print(count)