import sys
input = sys.stdin.readline

N = int(input())
S = list(input().strip())

stack = []; day = -1
for s in S:
    if s == '(':
        if stack and stack[-1] == ')':
            stack.pop()
        else:
            stack.append(s)
    elif s == ')':
        if stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(s)
    day = max(day, len(stack))
if len(stack) == 0: print(day)
else: print(-1)