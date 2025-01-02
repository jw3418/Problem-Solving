import sys
input = sys.stdin.readline

nA, nB = map(int, input().split())
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))
tmp1 = A - B; tmp2 = B - A
print(len(tmp1 | tmp2))