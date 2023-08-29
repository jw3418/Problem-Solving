x1, x2, n = map(int, input().split())

diff = abs(x1 - x2)
if x1 == x2:
    if n == 0:
        print("YES")
    else:
        print("NO")
    exit()

if x1 < x2:
    print("NO")
    exit()

if n == 0:
    if x1 == x2:
        print("YES")
    else:
        print("NO")
    exit()

if diff % n or diff % 2:
    print("NO")
elif diff // 2 < n:
    print("NO")
else:
    print("YES")