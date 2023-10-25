import sys

N  = int(sys.stdin.readline().strip())
have = set(list(sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
check = list(sys.stdin.readline().strip().split())
for c in check:
    if c in have: print(1, end=" ")
    else: print(0, end=" ")