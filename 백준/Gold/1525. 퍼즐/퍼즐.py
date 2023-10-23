import sys
from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

board = ""
for _ in range(3): tmp = sys.stdin.readline().strip(); tmp = tmp.replace(" ", ""); board += tmp

queue = deque([]); queue.append(board)
count = dict(); count[board] = 0

while queue:
    curr = queue.popleft()

    if curr == "123456780":
        print(count[curr])
        exit()
    
    idx = curr.index("0")
    x = idx // 3; y = idx % 3

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<3 and 0<=ny<3:
            nidx = nx*3 + ny
            next = list(curr)
            next[nidx], next[idx] = next[idx], next[nidx]
            next = "".join(next)

            if next not in count:
                queue.append(next)
                count[next] = count[curr] + 1
print(-1)