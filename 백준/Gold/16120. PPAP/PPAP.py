import sys
input = sys.stdin.readline

S = list(input().strip()); L = len(S)
stack = []
for i in range(L):
    stack.append(S[i])
    if len(stack) >= 4 and stack[-4:] == ['P', 'P', 'A', 'P']:
        for _ in range(3): stack.pop()
if len(stack) == 1 and stack[0] == 'P': print("PPAP")
else: print("NP")