import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for t in range(T):
    cmd = list(input().strip())
    L = len(cmd)
    left = []; right = []
    for i in range(L):
        if cmd[i] == '<':
            if left: right.append(left.pop())
        elif cmd[i] == '>':
            if right: left.append(right.pop())
        elif cmd[i] == '-':
            if left: left.pop()
        else:
            left.append(cmd[i])
    left.extend(reversed(right))
    print("".join(map(str, left)))