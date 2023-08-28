import sys
from collections import deque

def bfs():
    queue = deque([])
    queue.append(1); visit[1] += 1

    while queue:
        curr = queue.popleft()

        for after in adjacent[curr]:
            if visit[after] == -1:
                queue.append(after)
                visit[after] = visit[curr] + 1
                children[curr].add(after) #curr의 child는 after임


N = int(input())
adjacent = [[] for _ in range(N+1)]
for n in range(N-1):
    tmp = list(map(int, sys.stdin.readline()[:-1].split(' ')))
    adjacent[tmp[0]].append(tmp[1])
    adjacent[tmp[1]].append(tmp[0])
ans = list(map(int, sys.stdin.readline()[:-1].split()))

visit = [-1] * (N+1)
children = [set() for _ in range(N+1)]
bfs()

next_idx = 1
for i in ans:
    if next_idx == N:
        break

    children1 = set(ans[next_idx:next_idx+len(children[i])])
    children2 = children[i]

    if children1 != children2:
        print(0)
        exit()

    next_idx += len(children[i])
print(1)