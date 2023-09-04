import sys

string = sys.stdin.readline()[:-1]
bomb = sys.stdin.readline()[:-1]

stack = []
bomb_length = len(bomb)

for i in range(len(string)):
    stack.append(string[i])
    if ''.join(stack[-bomb_length:]) == bomb:
        for _ in range(bomb_length):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')