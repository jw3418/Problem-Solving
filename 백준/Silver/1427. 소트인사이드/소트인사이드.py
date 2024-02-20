import sys
input = sys.stdin.readline

N = list(map(int, list(input().strip())))
N.sort(reverse=True)
print("".join(map(str, N)))