import sys
input = sys.stdin.readline

def dfs(start, cnt):
    global num
    if cnt == N:
        result[num] = 1
        return
    for i in range(start, 4):
        num += roma[i]
        dfs(i, cnt+1)
        num -= roma[i]

N = int(input())
roma = [1, 5, 10, 50]
result = [0]*(50*20+1) # N 최대값 20
num = 0
dfs(0, 0)
print(sum(result))