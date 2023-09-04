import sys
from collections import deque

def bfs():
    queue = deque([])
    queue.append([s, ''])
    visit.add(s)

    while queue:
        currs, op = queue.popleft()

        if currs == t:
            print(op)
            return

        nexts = currs * currs
        if 1 <= nexts <= 10**9 and nexts not in visit:
            queue.append([nexts, op + '*'])
            visit.add(nexts)
        
        nexts = currs + currs
        if 1 <= nexts <= 10**9 and nexts not in visit:
            queue.append([nexts, op + '+'])
            visit.add(nexts)

        nexts = currs - currs
        if 1 <= nexts <= 10**9 and nexts not in visit:
            queue.append([nexts, op + '-'])
            visit.add(nexts)

        if currs != 0:
            nexts = currs // currs
            if 1 <= nexts <= 10**9 and nexts not in visit:
                queue.append([nexts, op + '/'])
                visit.add(nexts)
    print(-1)

s, t = map(int, sys.stdin.readline()[:-1].split())
if s == t:
    print(0)
else:
    visit = set()
    bfs()