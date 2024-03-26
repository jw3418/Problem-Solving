import sys
from collections import defaultdict
input = sys.stdin.readline

name = list(input().strip())
N = len(name)
ndict = defaultdict(int)
for i in range(N): ndict[name[i]] += 1

cnt = 0; mid = ''
for key, value in ndict.items():
    if value%2==1:
        cnt += 1
        if cnt >= 2:
            print("I'm Sorry Hansoo"); exit()
        else:
            mid = key

result = [] 
for key, value in sorted(ndict.items()):
    for v in range(value//2): result.extend(key)
print("".join(map(str, result))+mid+"".join(map(str, result[::-1])))