import sys
sys.setrecursionlimit(10**6)

def dfs(curr):
    global answer

    visit[curr] = True
    team.append(curr)

    if visit[adj[curr]]:
        if adj[curr] in team:
            answer -= len(team[team.index(adj[curr]):])
    else:
        dfs(adj[curr])


T = int(sys.stdin.readline()[:-1])
for t in range(T):
    N = int(sys.stdin.readline()[:-1])
    adj = [-1]; adj.extend(list(map(int, sys.stdin.readline()[:-1].split())))
    
    answer = N; visit = [False] * (N+1)
    for n in range(1, N+1):
        if not visit[n]:
            team = []; dfs(n)
    print(answer)