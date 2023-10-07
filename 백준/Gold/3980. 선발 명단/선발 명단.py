import sys

def dfs(depth, path):
    global max_score

    if depth == 11:
        max_score = max(max_score, sum(path))
        return
    
    for i in range(11):
        if not check[i] and S[depth][i] != 0:
            check[i] = True
            dfs(depth+1, path + [S[depth][i]])
            check[i] = False


C = int(sys.stdin.readline()[:-1])
for c in range(C):
    S = []
    for _ in range(11): S.append(list(map(int, sys.stdin.readline()[:-1].split())))
    
    max_score = 0
    check = [False]*11
    dfs(0, [])
    print(max_score)