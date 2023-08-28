import sys


N = int(input()); M = int(input())
distance = [[int(10e9) for _ in range(N+1)] for _ in range(N+1)]

for m in range(M):
    a, b, c = map(int, sys.stdin.readline()[:-1].split())
    distance[a][b] = min(c, distance[a][b]) #시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있음!

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            if a == b:
                distance[a][b] = 0
            else:
                distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])

for a in range(1, N+1):
    for b in range(1, N+1):
        if distance[a][b] == int(10e9):
            print(0, end=" ")
        else:
            print(distance[a][b], end=" ")
    print()