import sys
from collections import deque
input = sys.stdin.readline

N, W, L = map(int, input().split())
A = list(map(int, input().split())); A.reverse()

cnt = 0
queue = deque([0]*W)
while queue:
    cnt += 1
    queue.pop()
    if A:
        if sum(list(queue)) + A[-1] <= L:
            queue.appendleft(A.pop())
        else:
            queue.appendleft(0)
print(cnt)