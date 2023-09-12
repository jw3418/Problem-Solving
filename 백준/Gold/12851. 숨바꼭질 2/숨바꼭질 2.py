import sys
from collections import deque

N, K = map(int, sys.stdin.readline()[:-1].split())

if N >= K:
    print(N-K); print(1); exit()

queue = deque([]); queue.append(N)
visit = [-1]*100001; visit[N] = 0

way_cnt = 0
while queue:
    curr = queue.popleft()
    if curr == K:
        way_cnt += 1
    for next in (curr-1, curr+1, curr*2):
        if 0 <= next <= 100000:
            if visit[next] == -1 or visit[next] == visit[curr]+1: # 1) 방문한적 없는 경우 2) 방문한적 있는데 이동 시간 같은 경우
                visit[next] = visit[curr] + 1
                queue.append(next)

print(visit[K])
print(way_cnt)