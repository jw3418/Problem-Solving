import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
if N == 1: print(1); exit()
li = []
queue = deque([i for i in range(1, N+1)])

while len(queue) > 1:
    li.append(queue.popleft())
    tmp = queue.popleft(); queue.append(tmp)

str_ = " ".join(map(str, li)); str_ += " "; str_ += str(queue[0])
print(str_)

'''
1 2 3 4 5 6 7
1 / 3 4 5 6 7 2
1 3 / 5 6 7 2 4
1 3 5 / 7 2 4 6
1 3 5 7 / 4 6 2
1 3 5 7 4 / 2 6

'''