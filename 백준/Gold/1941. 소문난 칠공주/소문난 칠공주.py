import sys
from collections import deque
from itertools import combinations

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def ratioCheck(comb):
    y_cnt = 0
    for x, y in comb:
        if board[x][y] == 'Y': y_cnt += 1
    if y_cnt <= 3: return True
    else: return False

def adjacentCheck(comb):
    comb_set = set(comb)
    queue = deque([]); queue.append(comb[0])
    visit = [False]*7; visit[0] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if (nx, ny) in comb_set:
                nidx = comb.index((nx, ny))
                if not visit[nidx]:
                    visit[nidx] = True; queue.append((nx, ny))
    return False if False in visit else True


board = [list(sys.stdin.readline()[:-1]) for _ in range(5)]
pos = [(i, j) for i in range(5) for j in range(5)]; answer = 0
for comb in list(combinations(pos, 7)):
    if ratioCheck(comb): #비율로 pruning
        if adjacentCheck(comb):
            answer += 1
print(answer)