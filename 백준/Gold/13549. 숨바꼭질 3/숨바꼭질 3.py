import sys
from collections import deque

def bfs(N, K):
    queue = deque([]); queue.append(N)
    visit[N] = 0

    while queue:
        curr = queue.popleft()

        if curr == K:
            print(visit[curr])
            return

        if 0 <= curr*2 <= 100000 and visit[curr * 2] == -1: #순간이동은 0초 걸리기 때문에 우선 순위가 가장 높아야함
            queue.appendleft(curr * 2); visit[curr*2] = visit[curr]
        if 0 <= curr-1 <= 100000 and visit[curr - 1] == -1:
            queue.append(curr - 1); visit[curr-1] = visit[curr] + 1
        if 0 <= curr+1 <= 100000 and visit[curr + 1] == -1:
            queue.append(curr + 1); visit[curr+1] = visit[curr] + 1
        

         
N, K = map(int, input().split(' '))

visit = [-1] * (100000+1) #순간이동은 0초 걸리기 때문에 초기화를 0이 아닌 -1로 해줘야함
bfs(N, K)