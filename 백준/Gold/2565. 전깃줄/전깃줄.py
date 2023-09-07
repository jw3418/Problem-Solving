import sys

N = int(sys.stdin.readline()[:-1])
line = []
for n in range(N):
    line.append(list(map(int, sys.stdin.readline()[:-1].split())))
line.sort() # A를 기준으로 오름차순 정렬

dp = [1] * N
for i in range(1, N): #아래
    for j in range(0, i): #위
        if line[j][1] < line[i][1]: dp[i] = max(dp[i], dp[j]+1)
        
print(N - max(dp))