import sys
input = sys.stdin.readline

N = int(input())
D = list(map(int, input().split()))
sum_ = 0
if N == 1:
    D.sort()
    for i in range(0, 5): sum_ += D[i]
else:
    min_D = []
    min_D.append(min(D[0], D[5])); min_D.append(min(D[1], D[4])); min_D.append(min(D[2], D[3]))
    min_D.sort()
    
    sum_ += min_D[0] * ((N-2)*(N-2) + 4*(N-1)*(N-2))
    sum_ += sum(min_D[:2]) * (4*(N-2) + 4*(N-1))
    sum_ += sum(min_D) * 4
print(sum_)