import sys
import copy
from itertools import combinations
input = sys.stdin.readline

S = list(input().strip())
stack = []; result = []
for i in range(len(S)):
    if S[i] == '(': stack.append(i)
    elif S[i] == ')': result.append((stack.pop(), i))

answer = set()
for n in range(1, len(result)+1):
    for comb in combinations(result, n):
        comb = list(comb); S_li = list(S)
        for s, e in comb:
            S_li[s] = ''; S_li[e] = ''
        answer.add("".join(map(str, S_li)))
answer = list(answer)
answer.sort()
for ans in answer: print(ans)