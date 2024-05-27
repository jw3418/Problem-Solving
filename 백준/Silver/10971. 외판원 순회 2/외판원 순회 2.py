import sys
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for n in range(N)]

def dfs():
    global min_
    
    if len(nodes) == N:
        tmp = 0
        if W[nodes[N-1]][nodes[0]] == 0: return
        else: tmp += W[nodes[N-1]][nodes[0]]
        for i in range(1, N):
            if W[nodes[i-1]][nodes[i]] == 0: return
            else: tmp += W[nodes[i-1]][nodes[i]]
        min_ = min(min_, tmp)
    else:
        for n in range(N):
            if not visit[n]:
                nodes.append(n); visit[n] = True
                dfs()
                nodes.pop(); visit[n] = False

min_ = int(10e9)
nodes = []; visit = [False]*N
dfs()
print(min_)