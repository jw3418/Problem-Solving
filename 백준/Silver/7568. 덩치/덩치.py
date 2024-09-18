import sys
input = sys.stdin.readline

N = int(input())
li = []
for n in range(N):
    x, y = map(int, input().split())
    li.append((x, y))

re = []
for i in range(N):
    cnt = 1
    for j in range(N):
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            cnt += 1
    re.append(cnt)
print(*re)