import sys

T = int(sys.stdin.readline().strip())
for t in range(T):
    N = int(sys.stdin.readline().strip())
    li = [list(map(int, sys.stdin.readline().strip().split())) for n in range(N)]
    li.sort()
    
    answer = 1
    cur = li[0][1]
    for i in range(1, N):
        if cur > li[i][1]: answer += 1; cur = li[i][1]
    print(answer)