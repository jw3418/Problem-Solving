import sys

N = int(sys.stdin.readline()[:-1])
building = list(map(int, sys.stdin.readline()[:-1].split()))
stack = []
result = []
for i in range(N):
    flag = False
    while stack:
        if stack[-1][1] > building[i]:
            result.append(stack[-1][0] + 1); flag = True
            break
        else:
            stack.pop()
    if not flag: result.append(0)
    stack.append((i, building[i]))

for i in range(N):
    print(result[i], end=" ")
print()