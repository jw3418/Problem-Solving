import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set()
for n in range(N): S.add(input())

ans = 0
for m in range(M):
    if input() in S: ans+=1
print(ans)