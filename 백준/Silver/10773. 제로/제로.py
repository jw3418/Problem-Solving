import sys
input = sys.stdin.readline

K = int(input())
stack = []
for k in range(K):
    stack.append(int(input()))
    if stack[-1] == 0: stack.pop(); stack.pop()
print(sum(stack))