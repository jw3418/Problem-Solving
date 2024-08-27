import sys
input = sys.stdin.readline

N = int(input())
se = set()
for n in range(N):
    li = input().split()
    if li[1] == "enter":
        se.add(li[0])
    else:
        se.remove(li[0])
se = list(se); se.sort(reverse=True)
print("\n".join(map(str, se)))