import sys

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

N, M, K= map(int, sys.stdin.readline()[:-1].split())
add = [] #겨울에 추가되는 양분의 양
for n in range(N):
    add.append(list(map(int, sys.stdin.readline()[:-1].split())))
ground = [[5] * N for _ in range(N)] #양분 상황
tree = [[[] for _ in range(N)] for _ in range(N)]
for m in range(M):
    x, y, z = map(int, sys.stdin.readline()[:-1].split())
    tree[x-1][y-1].append(z)

for k in range(K): #K년
    #봄 + 여름
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                tree[i][j].sort() #나이순으로 정렬
                dead_tree = 0
                live_tree = []
                for age in tree[i][j]:
                    if ground[i][j] < age: #즉시 죽음
                        dead_tree += age//2
                    else:
                        ground[i][j] -= age
                        age += 1
                        live_tree.append(age)
                ground[i][j] += dead_tree
                tree[i][j].clear()
                tree[i][j].extend(live_tree)

    #가을
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                for age in tree[i][j]:
                    if age % 5 == 0:
                        for d in range(8):
                            nx = i + dx[d]; ny = j + dy[d]
                            if 0 <= nx < N and 0 <= ny < N:
                                tree[nx][ny].append(1)

    #겨울
    for i in range(N):
        for j in range(N):
            ground[i][j] += add[i][j]

result = 0
for i in range(N):
    for j in range(N):
        result += len(tree[i][j])
print(result)