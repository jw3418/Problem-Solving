import sys

def dfs(node):
    parent[node] = 'False' #지워야하는 노드를 'False'로 변경
    for i in range(N):
        if node == parent[i]: dfs(i) #지워야하는 노드의 자식 노드도 'False'로 변경
    

N = int(sys.stdin.readline()[:-1])
parent = list(map(int, sys.stdin.readline()[:-1].split()))
removed = int(sys.stdin.readline()[:-1])

dfs(removed) #지워야하는 노드들을 'False'로 변경

cnt = 0; parent_set = set(parent)
for i in range(N):
    if parent[i] != 'False' and i not in parent_set: cnt += 1
print(cnt)