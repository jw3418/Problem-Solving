import sys
input = sys.stdin.readline

def is_ccw(a, b, c):
    if (a[0] * b[1] + b[0] * c[1] + c[0] * a[1]) - (a[1] * b[0] + b[1] * c[0] + c[1] * a[0]) > 0:
        return True
    return False

def calculate_distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def convex_hull_heuristic(points):
    N = len(points)
    points = sorted(points)

    down = []
    for i in range(N):
        while len(down) > 1:
            if is_ccw(down[-2], down[-1], points[i]):
                break
            down.pop()
        down.append(points[i])

    up = []
    for i in range(N - 1, -1, -1):
        while len(up) > 1:
            if is_ccw(up[-2], up[-1], points[i]):
                break
            up.pop()
        up.append(points[i])

    hull = down[:-1] + up[:-1]
    size = len(hull)

    ax = ay = 0
    for x, y in hull:
        ax += x
        ay += y
    ax /= size
    ay /= size

    rat = 0.1
    for _ in range(5000):
        D = I = -1
        for i in range(size):
            d = calculate_distance([ax, ay], hull[i])
            if D < d:
                D = d
                I = i

        ax += (hull[I][0] - ax) * rat
        ay += (hull[I][1] - ay) * rat
        rat *= 0.995

    result = [format(ax, '.3f'), format(ay, '.3f'),
              format(max(calculate_distance([ax, ay], hull[i]) for i in range(size)), '.3f')]
    print('0.000' if result[0] == '-0.000' else result[0], '0.000' if result[1] == '-0.000' else result[1])
    print(result[2])

convex_hull_heuristic([list(map(float, line.split())) for line in sys.stdin.readlines()[1:]])