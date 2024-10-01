import sys
input = sys.stdin.readline

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

K = int(input())
li = []
for _ in range(6): li.append(list(map(int, input().split())))

horizontal = []; vertical = []
for i in range(6):
    if li[i][0] == 1 or li[i][0] == 2: horizontal.append(li[i][1])
    else: vertical.append(li[i][1])
rect = max(horizontal)*max(vertical)

black = set()
black.add("13") # 우하 1->3
black.add("41") # 상우 4->1
black.add("24") # 좌상 2->4
black.add("32") # 하좌 3->2
for i in range(6):
    if i == 5:
        str_ = str(li[i][0]) + str(li[0][0])
        if str_ in black:
            rect -= li[i][1]*li[0][1]
            break
    else:
        str_ = str(li[i][0]) + str(li[i+1][0])
        if str_ in black:
            rect -= li[i][1]*li[i+1][1]
            break
print(rect*K)