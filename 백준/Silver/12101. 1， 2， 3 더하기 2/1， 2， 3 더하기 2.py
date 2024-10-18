import sys
input = sys.stdin.readline

def dfs(li):
    global flag
    if len(li) > N: return
    if sum(li) == N:
        result.append(li)
        if len(result) == K:
            flag = True
            print("+".join(map(str, result[K-1])))
            exit()
        return
    for i in range(3):
        dfs(li+[num[i]])

N, K = map(int, input().split())
num = [1, 2, 3]
result = []
flag = False
dfs([])
if not flag: print(-1)