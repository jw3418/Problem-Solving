import sys
from collections import deque
input = sys.stdin.readline

A, B, C = map(int, input()[:-1].split())
answer = []

queue = deque([]); queue.append((0, 0, C))
visit = [[[False]*(C+1) for _ in range(B+1)] for _ in range(A+1)]; visit[0][0][C] = True

while queue:
    a, b, c = queue.popleft()
    if a == 0: answer.append(c)

    #a -> b
    water = min(a, B-b)
    if not visit[a-water][b+water][c]:
        visit[a-water][b+water][c] = True
        queue.append((a-water, b+water, c))

    #a -> c
    water = min(a, C-c)
    if not visit[a-water][b][c+water]:
        visit[a-water][b][c+water] = True
        queue.append((a-water, b, c+water))

    #b -> a
    water = min(b, A-a)
    if not visit[a+water][b-water][c]:
        visit[a+water][b-water][c] = True
        queue.append((a+water, b-water, c))

    #b -> c
    water = min(b, C-c)
    if not visit[a][b-water][c+water]:
        visit[a][b-water][c+water] = True
        queue.append((a, b-water, c+water))

    #c -> a
    water = min(c, A-a)
    if not visit[a+water][b][c-water]:
        visit[a+water][b][c-water] = True
        queue.append((a+water, b, c-water))

    #c -> b
    water = min(c, B-b)
    if not visit[a][b+water][c-water]:
        visit[a][b+water][c-water] = True
        queue.append((a, b+water, c-water))

answer.sort()
print(" ".join(map(str, answer)))