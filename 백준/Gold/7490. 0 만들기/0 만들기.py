import sys

def dfs(path, depth):
    if depth == N-1:
        if check(path): print(path)
        return

    n = depth+2
    dfs(path+' '+str(n), depth+1)
    dfs(path+'+'+str(n), depth+1)
    dfs(path+'-'+str(n), depth+1)

def check(path):
    path = path.replace(' ', '')
    if eval(path) == 0: return True
    else: return False


T = int(sys.stdin.readline()[:-1])
for t in range(T): N = int(sys.stdin.readline()[:-1]); dfs("1", 0); print()