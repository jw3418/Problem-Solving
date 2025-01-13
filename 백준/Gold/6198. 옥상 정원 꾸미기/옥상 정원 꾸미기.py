import sys
input = sys.stdin.readline

N = int(input())
H = [int(input()) for n in range(N)]

stack = []
ans = 0
for i in range(N):
    while stack and stack[-1] <= H[i]: stack.pop() #오른쪽건물의 높이가 현재건물과 같거나 높으면 제거
    ans += len(stack)
    stack.append(H[i])
print(ans)