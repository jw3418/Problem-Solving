import sys
input = sys.stdin.readline

N = int(input())
H = [int(input()) for n in range(N)]

stack = []
ans = 0
for i in range(N):
    idx = i
    while stack and stack[-1][1] > H[i]:
        idx, height = stack.pop()
        ans = max(ans, (i-idx) * height)
    stack.append((idx, H[i]))

while stack:
    idx, height = stack.pop()
    ans = max(ans, (N-idx) * height)

print(ans)