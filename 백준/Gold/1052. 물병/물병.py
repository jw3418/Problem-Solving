import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cnt = 0 
while bin(N).count("1") > K:
    cnt += 1; N += 1
print(cnt)