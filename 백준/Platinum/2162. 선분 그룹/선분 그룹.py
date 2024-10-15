import sys
from collections import Counter
input = sys.stdin.readline

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a); b = find(b)
    if a < b: parent[b] = a
    else: parent[a] = b

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

def direction(a: Point, b: Point, c: Point):
    dxab = b.x - a.x
    dxac = c.x - a.x
    dyab = b.y - a.y
    dyac = c.y - a.y

    if dxab * dyac < dyab * dxac:
        dir = 1
    elif dxab * dyac > dyab * dxac:
        dir = -1
    else:
        if dxab == 0 and dyab == 0:
            dir == 0
        if dxab * dxac < 0 or dyab * dyac < 0:
            dir = -1
        elif dxab * dxab + dyab * dyab >= dxac * dxac + dyac * dyac:
            dir = 0
        else:
            dir = 1
    return dir

def intersection(l1: Line, l2: Line):
    if direction(l1.p1, l1.p2, l2.p1) * direction(l1.p1, l1.p2, l2.p2) <= 0 and direction(l2.p1, l2.p2, l1.p1) * direction(l2.p1, l2.p2, l1.p2) <= 0:
        return True
    return False

N = int(input())

lines = []
parent = [i for i in range(N)]
for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    line = Line(Point(x1, y1), Point(x2, y2))
    lines.append(line)

for i in range(N):
    for j in range(i+1, N):
        if intersection(lines[i], lines[j]):
            union(i, j)

for i in range(N): find(i)

cnt = Counter(parent)
print(len(cnt))
print(max(cnt.values()))