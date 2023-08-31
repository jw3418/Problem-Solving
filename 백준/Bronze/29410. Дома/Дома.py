import sys

N, a, b = map(int, sys.stdin.readline()[:-1].split())

cost = 0
for _ in range(N):
    tmp = list(map(int, sys.stdin.readline()[:-1].split()))
    a_i = tmp[0]; c_js = tmp[1:]
    
    for c_j in c_js:
        c_j = bin(c_j)[2:]
        zero = c_j.count('0'); one = len(c_j) - zero
        cost += zero*a + one*b

print(cost)