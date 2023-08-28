import sys
from collections import deque

def calD(A):
    return (A * 2) % 10000

def calS(A):
    return (A - 1) % 10000

def calL(A):
    return A // 1000 + (A % 1000) * 10

def calR(A):
    return A // 10 + (A % 10) * 1000


def bfs(A, B):
    queue = deque([])
    queue.append([A, ''])
    visit[A] = True

    while queue:
        currA, trace = queue.popleft()

        if currA == B:
            print(trace)
            break

        nextA = calD(currA)
        if not visit[nextA]:
            visit[nextA] = True
            queue.append([nextA, trace + 'D'])

        nextA = calS(currA)
        if not visit[nextA]:
            visit[nextA] = True
            queue.append([nextA, trace + 'S'])

        nextA = calL(currA)
        if not visit[nextA]:
            visit[nextA] = True
            queue.append([nextA, trace + 'L'])
            
        nextA = calR(currA)
        if not visit[nextA]:
            visit[nextA] = True
            queue.append([nextA, trace + 'R'])

T = int(input())
for _ in range(T):
    A, B = map(int, sys.stdin.readline()[:-1].split())
    visit = [False for i in range(10001)]
    bfs(A, B)