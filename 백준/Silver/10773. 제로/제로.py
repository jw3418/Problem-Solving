import sys
input = sys.stdin.readline

K = int(input())
stack = []
for k in range(K):
    n = int(input())
    if n == 0: stack.pop()
    else: stack.append(n)
print(sum(stack))