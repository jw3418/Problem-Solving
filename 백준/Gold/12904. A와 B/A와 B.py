import sys

S = list(sys.stdin.readline()[:-1])
T = list(sys.stdin.readline()[:-1])

result = False
while T:
    if S == T:
        result = True
        break
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T.reverse()

if result:
    print(1)
else:
    print(0)