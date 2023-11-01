import sys

N = sys.stdin.readline().strip()

if "0" not in N: print(-1)
else:
    sum_ = 0
    for i in range(len(N)):
        sum_ += int(N[i])
    
    if sum_ % 3 != 0: print(-1)

    else:
        sorted_N = sorted(N, reverse=True)
        print("".join(sorted_N))