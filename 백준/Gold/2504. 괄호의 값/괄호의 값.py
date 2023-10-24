import sys

string = sys.stdin.readline().strip()

stack = []
answer = 0
weight = 1
for i in range(len(string)):
    if string[i] == '(':
        stack.append(string[i])
        weight *= 2

    elif string[i] == '[':
        stack.append(string[i])
        weight *= 3

    elif string[i] == ')':
        if not stack or stack[-1] == '[': answer = 0; break
        if string[i-1] == '(':
            answer += weight
        stack.pop()
        weight //= 2

    elif string[i] == ']':
        if not stack or stack[-1] == '(': answer = 0; break
        if string[i-1] == '[':
            answer += weight
        stack.pop()
        weight //= 3

if stack: print(0)
else: print(answer)