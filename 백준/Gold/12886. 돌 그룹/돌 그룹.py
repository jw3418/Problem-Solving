import sys
from collections import deque

def bfs():
    global A, B, C, total
    queue = deque()
    queue.append([A, B])
    visit[A][B] = True

    while queue:
        currA, currB = queue.popleft()
        currC = total - (currA + currB)
        if currA == currB == currC:
            print(1)
            return
        
        for nextA, nextB in [currA, currB], [currB, currC], [currA, currC]:
            if nextA > nextB:
                nextA -= nextB; nextB += nextB
            elif nextA < nextB:
                nextB -= nextA; nextA += nextA
            else:
                continue
            if not visit[nextA][nextB]:
                queue.append([nextA, nextB])
                visit[nextA][nextB] = True
    print(0) 


A, B, C = map(int, sys.stdin.readline()[:-1].split())
total = A + B + C
visit = [[False for _ in range(total + 1)] for _ in range(total + 1)]

if total % 3 != 0:
    print(0)
else:
    bfs()