import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(cur):
    for nex in adj[cur]:
        score[nex] += score[cur]
        dfs(nex)

N, M = map(int, input().strip().split())

adj = [[] for n in range(N+1)]
employer = [0]; employer.extend(list(map(int, input().strip().split())))
for n in range(1, N+1):
    if employer[n] != -1: adj[employer[n]].append(n)

score = [0]*(N+1)
for m in range(M):
    i, w = map(int, input().strip().split())
    score[i] += w

dfs(1)
print(" ".join(map(str, score[1:])))