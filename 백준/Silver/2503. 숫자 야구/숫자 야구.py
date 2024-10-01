import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
candi = list(permutations(li, 3))
garbage = set()
for n in range(N):
    num, strike, ball = map(int, input().split())
    num = list(map(int, list(str(num))))
    for i in range(len(candi)):
        s = 0; b = 0
        for j in range(3):
            if candi[i][j] == num[j]: s += 1
            elif candi[i][j] in num: b += 1
        if (s, b) != (strike, ball): garbage.add(i)
ans = 0
for i in range(len(candi)):
    if i not in garbage: ans+=1
print(ans)