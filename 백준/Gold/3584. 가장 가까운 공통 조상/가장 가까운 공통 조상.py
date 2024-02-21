import sys
input = sys.stdin.readline

T = int(input().strip())
for t in range(T):
    N = int(input().strip())
    parents = [0] * (N+1)
    for _ in range(N-1): A, B = map(int, input().strip().split()); parents[B] = A
    c1, c2 = map(int, input().strip().split())
    c1_p, c2_p = [c1], [c2]
    while parents[c1]: c1_p.append(parents[c1]); c1 = parents[c1]
    while parents[c2]: c2_p.append(parents[c2]); c2 = parents[c2]
    
    c1_idx = len(c1_p)-1; c2_idx = len(c2_p)-1
    while c1_p[c1_idx] == c2_p[c2_idx]: c1_idx -= 1; c2_idx -= 1
    print(c1_p[c1_idx+1])