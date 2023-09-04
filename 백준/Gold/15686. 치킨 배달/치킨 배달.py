import sys

def dfs(depth, index_flag):
    global global_distance

    if depth == M:
        #print(now_chicken)
        total_distance = 0
        for i in range(len(home)):
            distance = int(1e9)
            for j in range(len(now_chicken)):
                distance = min(distance, abs(home[i][0] - now_chicken[j][0]) + abs(home[i][1] - now_chicken[j][1]))
            total_distance += distance
        global_distance = min(global_distance, total_distance)
        return

    for i in range(index_flag, len(chicken)):
        chick = chicken[i]
        if chick not in now_chicken:
            now_chicken.append(chick)
            dfs(depth + 1, i + 1)
            now_chicken.pop()

N, M = map(int, sys.stdin.readline()[:-1].split())
home = []
chicken = []
for i in range(N):
    tmp = list(map(int, sys.stdin.readline()[:-1].split()))
    for j in range(N):
        if tmp[j] == 1:
            home.append([i, j])
        if tmp[j] == 2:
            chicken.append([i, j])

global_distance = int(1e9)
now_chicken = []; visit = [[0 for _ in range(N)] for __ in range(N)]
dfs(0, 0)
print(global_distance)