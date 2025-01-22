import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
s1 = []; s2 = []; s3 = []; s4 = []
stack = [s1, s2, s3, s4]

for a in A:
    flag = False
    for s in stack:
        if s and s[-1] < a:
            s.append(a)
            flag = True
            break
        if not s:
            s.append(a)
            flag = True
            break
    if not flag: print("NO"); exit()
print("YES")