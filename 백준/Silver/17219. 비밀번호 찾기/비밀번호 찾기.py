import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dict_ = dict()
for n in range(N):
    a, b = map(str, input().split())
    dict_[a] = b
for m in range(M):
    a = input().strip()
    print(dict_[a])