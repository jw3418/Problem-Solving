import sys
from itertools import combinations
input = sys.stdin.readline

def dfs(idx):
    global flag
    if idx == 15:
        sum_ = 0
        for res in result: sum_ += sum(res)
        if sum_ == 0: flag = True
        else: flag = False
        return

    a, b = match[idx][0], match[idx][1]

    if result[a][0] > 0 and result[b][2] > 0:
        result[a][0] -= 1; result[b][2] -= 1 #a승b패
        dfs(idx+1)
        result[a][0] += 1; result[b][2] += 1
    if result[a][1] > 0 and result[b][1] > 0:
        result[a][1] -= 1; result[b][1] -= 1 #a무b무
        dfs(idx+1)
        result[a][1] += 1; result[b][1] += 1
    if result[a][2] > 0 and result[b][0] > 0:
        result[a][2] -= 1; result[b][0] -= 1 #a패b승
        dfs(idx+1)
        result[a][2] += 1; result[b][0] += 1

ans = []
match = list(combinations([0, 1, 2, 3, 4, 5], 2)) #가능한 매치에 대해 브루트포스
for _ in range(4):
    tmp = list(map(int, input().split()))
    result = [tmp[i:i+3] for i in range(0, 15+1, 3)]
    flag = False
    dfs(0)
    if flag: ans.append(1)
    else: ans.append(0)
print(*ans)