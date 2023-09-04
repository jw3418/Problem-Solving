import sys
from collections import deque


def left(index, direction):
    if index < 0:
        return
    if Gears[index][2] == Gears[index+1][6]:
        return
    if Gears[index][2] != Gears[index+1][6]:
        left(index-1, -direction)
        Gears[index].rotate(-direction)

def right(index, direction):
    if index > T-1:
        return
    if Gears[index][6] == Gears[index-1][2]:
        return
    if Gears[index][6] != Gears[index-1][2]:
        right(index+1, -direction)
        Gears[index].rotate(-direction)

T = int(sys.stdin.readline()[:-1])
Gears = []
for t in range(T):
    Gears.append(deque(list(map(int, list(sys.stdin.readline()[:-1])))))

K = int(sys.stdin.readline()[:-1])
method = []
for k in range(K):
    tmp = list(map(int, sys.stdin.readline()[:-1].split()))
    method.append((tmp[0]-1, tmp[1]))

for k in range(K):
    index, direction = method[k]
    left(index - 1, direction)
    right(index + 1, direction)
    Gears[index].rotate(direction)

result = 0
for gear in Gears:
    if gear[0] == 1:
        result += 1
print(result)