import sys

N, K = map(int, sys.stdin.readline().strip().split()); number = list(map(int, list(sys.stdin.readline().strip())))
stack = []
for i in range(N):
    while stack and stack[-1] < number[i] and K > 0: stack.pop(); K -= 1 #가장 큰 숫자가 앞쪽에 위치하도록
    stack.append(number[i])
if K>0: print("".join(map(str, stack[:-K])))
else: print("".join(map(str, stack)))