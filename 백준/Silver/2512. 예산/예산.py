import sys

N = int(sys.stdin.readline().strip())
city = list(map(int, sys.stdin.readline().strip().split()))
budget = int(sys.stdin.readline().strip())
start, end = 0, max(city)

while start <= end:
    mid = (start + end) // 2
    
    tmp = 0
    for c in city:
        if c > mid: tmp += mid
        else: tmp += c

    if tmp <= budget: start = mid + 1
    else: end = mid - 1
print(end)