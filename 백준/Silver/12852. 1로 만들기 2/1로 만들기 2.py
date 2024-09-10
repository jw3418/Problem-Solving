import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

queue = deque([])
queue.append([N])
min_len = int(10e9)
while queue:
    li = queue.popleft(); x = li[-1]
    if x == 1:
        print(len(li)-1)
        print(*li)
        break
    elif x > 1:
        if x % 3 == 0:
            queue.append(li+[x//3])
        if x % 2 == 0:
            queue.append(li+[x//2])
        queue.append(li+[x-1])