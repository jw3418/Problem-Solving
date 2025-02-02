import sys
input = sys.stdin.readline

N = int(input())
max_H = 0; max_Idx = 0; end_Idx = 0
data = [0] * 1001
for n in range(N):
    Idx, H = map(int, input().split())
    data[Idx] = H
    if H > max_H:
        max_H = H
        max_Idx = Idx
    end_Idx = max(end_Idx, Idx)

stack  = []
ans = 0
for i in range(max_Idx+1):
    if not stack: stack.append(data[i])
    else:
        if stack[-1] < data[i]:
            stack.pop()
            stack.append(data[i])
    ans += stack[-1]

stack = []
for i in range(end_Idx, max_Idx, -1):
    if not stack: stack.append(data[i])
    else:
        if stack[-1] < data[i]:
            stack.pop()
            stack.append(data[i])
    ans += stack[-1]
print(ans)