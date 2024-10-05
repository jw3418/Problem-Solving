import sys
input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

N = int(input())
cost = [list(map(int, input().split())) for n in range(N)]

def test(x, y, visit):
    if (x, y) in visit: return False
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if (nx, ny) in visit: return False
    return True

def dfs(visit, total_cost):
    global ans
    if total_cost > ans: return
    if len(visit) == 15:
        ans = min(ans, total_cost)
    else:
        for x in range(1, N-1):
            for y in range(1, N-1):
                tvisit = [(x, y)]
                ttotal_cost = cost[x][y]
                if test(x, y, visit):
                    for i in range(4):
                        nx, ny = x+dx[i], y+dy[i]
                        ttotal_cost += cost[nx][ny]
                        tvisit.append((nx, ny))
                    dfs(visit + tvisit, total_cost+ttotal_cost)

ans = int(10e9)
dfs([], 0)
print(ans)