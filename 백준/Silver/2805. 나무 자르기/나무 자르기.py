import sys

N, M = map(int, sys.stdin.readline()[:-1].split())
tree = list(map(int, sys.stdin.readline()[:-1].split()))

start = 1; end = max(tree)
while start <= end:
    mid = (start+end)//2

    sum_ = 0
    for t in tree:
        if t > mid: sum_ += t - mid
    
    if sum_ >= M: start = mid + 1
    else: end = mid - 1
print(end)