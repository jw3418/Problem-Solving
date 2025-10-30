import sys
from collections import deque
input = sys.stdin.readline

def dfs(cur, depth):
    global max_depth
    
    visited[cur] = True
    Tree[cur][3] = depth
    if max_depth < depth:
        max_depth = depth

    for i in range(2):
        if not visited[Tree[cur][i]]:
            dfs(Tree[cur][i], depth+1)

def in_order(cur):
    global order
    
    if cur:
        in_order(Tree[cur][0])
        Tree[cur][4] = order; order += 1
        in_order(Tree[cur][1])


N = int(input())
Tree = [[0, 0, 0, 0, 0] for _ in range(N+1)] # [left, right, parent, depth, height]
for _ in range(N):
    node, left, right = map(int, input().split())
    if left == -1: left = 0
    if right == -1: right = 0

    Tree[node][0] = left; Tree[node][1] = right
    Tree[left][2] = node
    Tree[right][2] = node


root_num = 0
for i in range(1, N+1):
    if Tree[i][2] == 0:
        root_num = i
        break

max_depth = 0
visited = [False] * (N+1); visited[0] = True
dfs(root_num, 1)

order = 1
in_order(root_num)

nums_by_depths = [[] for _ in range(max_depth+1)]
for i in range(1, N+1):
    nums_by_depths[Tree[i][3]].append(Tree[i][4])

result = []
for i in range(len(nums_by_depths)):
    if len(nums_by_depths[i]) <= 1:
        result.append(1)
    else:
        result.append(max(nums_by_depths[i]) - min(nums_by_depths[i]) + 1)
print(result.index(max(result), 1), max(result))