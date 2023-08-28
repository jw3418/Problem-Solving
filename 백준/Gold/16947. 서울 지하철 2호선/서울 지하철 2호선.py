import sys
from collections import deque
sys.setrecursionlimit(100000)

def check_cycle(curr, start, depth):
    visit[curr] = True
    for next in adjacent[curr]:
        if not visit[next]:
            check_cycle(next, start, depth+1)
        elif next == start and depth >= 2: #cycle이 형성된 경우
            cycle.add(next)
            return

def distance():
    dist_ans = [-1] * (N+1)
    queue = deque([])

    for i in range(1, N+1):
        if i in cycle: #cycle에 속하는 node에서 bfs 시작
            queue.append(i)
            dist_ans[i] = 0

    while queue:
        curr = queue.popleft()
        for next in adjacent[curr]:
            if dist_ans[next] == -1:
                queue.append(next)
                dist_ans[next] = dist_ans[curr] + 1
    
    for i in range(1, N+1):
        print(dist_ans[i], end=' ')



N = int(input())
adjacent = [[] for _ in range(N+1)]
for i in range(N):
    tmp0, tmp1 = map(int, sys.stdin.readline()[:-1].split(' '))
    adjacent[tmp0].append(tmp1)
    adjacent[tmp1].append(tmp0)

cycle = set()
for x in range(1, N+1):
    visit = [False] * (N+1)
    check_cycle(x, x, 0)

distance()