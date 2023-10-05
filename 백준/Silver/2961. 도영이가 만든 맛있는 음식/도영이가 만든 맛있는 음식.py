import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
tastes = []
for n in range(N): S, B = map(int, input()[:-1].split()); tastes.append((S, B))

def dfs(idx, visit, s, b):
    global min_diff
    if idx != 0: min_diff = min(min_diff, abs(s-b))

    for i in range(idx, N):
        if not visit[i]:
            visit[i] = True
            dfs(idx+1, visit, s*tastes[i][0], b+tastes[i][1])
            visit[i] = False


min_diff = int(10e9); visit = [False]*N
dfs(0, visit, 1, 0)
print(min_diff)