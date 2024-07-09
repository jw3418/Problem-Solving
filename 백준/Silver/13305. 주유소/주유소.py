import sys
input = sys.stdin.readline

N = int(input())
dist = list(map(int, input().split()))
KMpL = list(map(int, input().split()))

min_kmpl = KMpL[0]
ans = 0
for i in range(N-1):
    if min_kmpl > KMpL[i]:
        min_kmpl = KMpL[i]
    ans += min_kmpl * dist[i]
print(ans)