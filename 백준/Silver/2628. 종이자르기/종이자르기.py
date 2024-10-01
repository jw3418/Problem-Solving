import sys
input = sys.stdin.readline

V, H = map(int, input().split())
N = int(input())
hori = [0, H]; vert = [0, V]
for n in range(N):
    _, num = map(int, input().split())
    if _ == 0: hori.append(num)
    else: vert.append(num)
hori.sort(); vert.sort()
# print(hori, vert)
hmax = 0
for i in range(len(hori)-1):
    hmax = max(hmax, hori[i+1]-hori[i])
vmax = 0
for i in range(len(vert)-1):
    vmax = max(vmax, vert[i+1]-vert[i])
print(hmax*vmax)