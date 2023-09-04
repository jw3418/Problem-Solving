import sys

tmp = list(map(int, sys.stdin.readline()[:-1].split(' ')))
N = tmp[0]; M = tmp[1]
adjacent = [[] for _ in range(N)]
for _ in range(M):
    t0, t1 = map(int, sys.stdin.readline()[:-1].split(' '))
    adjacent[t0].append(t1)
    adjacent[t1].append(t0)

visit = [False] * N
possible_flag = 0
def dfs(start, depth):
    global possible_flag
    visit[start] = True
    if depth == 5:
        possible_flag = 1
        return
    for i in range(len(adjacent[start])):
        if not visit[adjacent[start][i]]:
            dfs(adjacent[start][i], depth+1)
    visit[start] = False

for x in range(N):
    dfs(x, 1)

if possible_flag == 1:
    print(1)
else:
    print(0)