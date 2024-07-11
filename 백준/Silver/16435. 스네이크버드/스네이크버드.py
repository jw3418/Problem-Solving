import sys
input = sys.stdin.readline

N, L = map(int, input().split())
H = list(map(int, input().split()))
H.sort()

for h in H:
    if L >= h: L+=1
print(L)