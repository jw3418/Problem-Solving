import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [tuple(list(map(int, input().split()))) for m in range(M)]
distance = [int(10e9)] * (N+1)

def BellmanFord(s):
    distance[s] = 0

    for n in range(1, N+1): # N번 반복
        for m in range(M): # 매번 모든 간선 확인
            cur, nex, dist = graph[m]
            if distance[cur] != int(10e9):
                if distance[nex] > distance[cur]+dist:
                    distance[nex] = distance[cur]+dist
                    if n == N: # N번째에도 갱신된다면 음수 사이클 존재
                        return True
    return False

NegativeCycle = BellmanFord(1)
if NegativeCycle: print(-1)
else:
    for n in range(2, N+1):
        if distance[n] == int(10e9): print(-1)
        else: print(distance[n])