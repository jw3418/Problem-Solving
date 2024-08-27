import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))

queue = deque([])
for i in range(N):
    if queue and queue[0][0] <= i-L:
        queue.popleft()

    while len(queue) >= 1 and queue[-1][1] > A[i]:
        queue.pop()

    queue.append((i, A[i]))
    print(queue[0][1], end=" ")