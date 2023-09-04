import sys
sys.setrecursionlimit(1000000)

def dfs(start, color):
        global flag
        visit[start] = color
        for i in range(len(adjacent[start])):
            if visit[adjacent[start][i]] == 0:
                dfs(adjacent[start][i], -color) # depth마다 color 값을 1과 -1로 번갈아가면서 할당
                if visit[start] == visit[adjacent[start][i]]:
                    flag = 1
                    return
            elif visit[start] == visit[adjacent[start][i]]:
                flag = 1
                return

K = int(input())
for k in range(K):
    tmp = list(map(int, sys.stdin.readline()[:-1].split(' ')))
    N = tmp[0]; M = tmp[1]
    adjacent = [[] for _ in range(N+1)]
    for _ in range(M):
        t0, t1 = map(int, sys.stdin.readline()[:-1].split(' '))
        adjacent[t0].append(t1)
        adjacent[t1].append(t0)

    flag = 0
    visit = [0] * (N+1)
    for x in range(1, N+1):
        if visit[x] == 0:
            dfs(x, 1)

    if flag == 1:
        print("NO")
    else:
        print("YES")