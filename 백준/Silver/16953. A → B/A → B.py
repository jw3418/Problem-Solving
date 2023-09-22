import sys

def dfs(start, depth):
    global count

    if start == B: count = min(count, depth); return
    if start > B: return
    else:
        next = start * 2
        if next not in visit: visit.add(next); dfs(next, depth+1)
        next = start*10+1
        if next not in visit: visit.add(next); dfs(next, depth+1)        


A, B = map(int, sys.stdin.readline()[:-1].split())
visit = set(); visit.add(A); count = int(10e9)
dfs(A, 0)
if count == int(10e9): print(-1)
else: print(count+1)