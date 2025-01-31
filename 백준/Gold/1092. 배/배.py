import sys
input = sys.stdin.readline

N = int(input())
C_w = list(map(int, input().split())); C_w.sort()
M = int(input())
B_w = list(map(int, input().split())); B_w.sort(reverse=True)
# print(C_w, B_w)

minute = 0
if B_w[0] > C_w[-1]: minute = -1
else:
    while B_w:
        for c in range(N): #작은 크레인부터 순회
            if B_w and C_w[c] < B_w[-1]: continue
            for b in range(len(B_w)): #큰 박스부터 순회
                if C_w[c] >= B_w[b]:
                    del B_w[b]; break
        minute += 1
print(minute)

'''
3
10 6 5
11
6 8 9 6 8 6 9 6 8 6 9
//6

4
1 2 3 4
8
1 1 2 2 3 3 4 4
//2
'''