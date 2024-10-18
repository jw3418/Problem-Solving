import sys
input = sys.stdin.readline

def dfs(num):
    if len(num) > 0: result.append(int(num))
    
    for i in range(10):
        if len(num) == 0 or i < int(num[-1]):
            dfs(num+str(i))

N = int(input())
result = []
dfs("")
if len(result) < N: print(-1)
else:
    result.sort()
    print(result[N-1])