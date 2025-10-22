import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    C = int(input())
    div = [25, 10, 5, 1]
    ans = [0, 0, 0, 0]
    for i, d in enumerate(div):
        ans[i] = C // d
        C %= d
    print(" ".join(map(str, ans)))