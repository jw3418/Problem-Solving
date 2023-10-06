import sys
input = sys.stdin.readline

def dfs(idx, first, second):
    global result

    if visit[idx] == False:
        visit[idx] = True
        for num in graph[idx]:
            first.add(idx); second.add(num)
            if first == second:
                tmp = set(first); result = result | tmp
            dfs(num, first, second)

N = int(input())
graph = dict()
for n in range(1, N+1):
    m = int(input())
    if n in graph: graph[n].append(m)
    else: graph[n] = [m]

result = set()
for i in range(1, N+1):
    if i not in result:
        visit = [False] * (N+1)
        dfs(i, set(), set())

result = list(result); result.sort()
print(len(result))
for r in result: print(r)