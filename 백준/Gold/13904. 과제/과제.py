import sys

N = int(sys.stdin.readline().strip()); assn = []; visit = [False]*1001
for n in range(N): assn.append(list(map(int, sys.stdin.readline().strip().split())))

assn.sort(key=lambda x:x[1], reverse=True)

answer = 0
for d, w in assn:
    while d>0 and visit[d]: d-=1
    if d != 0:
        visit[d] = True; answer += w
print(answer)