import sys

tmp = list(map(int, sys.stdin.readline().strip().split()))
tmp.sort()
print(tmp[1])