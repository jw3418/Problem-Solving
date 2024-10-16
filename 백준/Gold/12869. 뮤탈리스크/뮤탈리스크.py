import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

queue = deque([]); queue.append(S+[0])
visit = set(); visit.add(tuple(S))
min_cnt = int(10e9)
while queue:
    cur = queue.popleft()
    flag = True
    for i in range(N):
        if cur[i]>0: flag = False; break
    if flag: min_cnt = min(min_cnt, cur[N])
    else:
        for nex in list(permutations(cur[:N], N)):
            nex = list(nex)
            damage = 9
            for n in range(N):
                nex[n] -= damage; damage /= 3
            if tuple(nex) not in visit:
                queue.append(list(nex)+[cur[N]+1])
                visit.add(tuple(nex))
print(min_cnt)