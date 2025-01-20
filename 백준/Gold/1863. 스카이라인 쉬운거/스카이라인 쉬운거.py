import sys
input = sys.stdin.readline

N = int(input())
sky = []
for n in range(N):
    x, y = map(int, input().split())
    sky.append(y)
sky.append(0)

stack = []
cnt = 0
for cy in sky:
    ty = cy
    while stack and stack[-1] > cy:
        if stack[-1] != ty:
            ty = stack[-1]
            cnt += 1
        stack.pop()
    stack.append(cy)
print(cnt)