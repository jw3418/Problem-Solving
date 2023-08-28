tmp = list(map(int, input().split(' ')))
N = tmp[0]; M = tmp[1]; x = tmp[2]; y = tmp[3]; K = tmp[4]

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split(' '))))

cmd = []
cmd = list(map(int, input().split(' ')))

dice = [0, 0, 0, 0, 0, 0] # dice[0]가 윗면임

def turn(direction):
    d_0 = dice[0]; d_1 = dice[1]; d_2 = dice[2]; d_3 = dice[3]; d_4 = dice[4]; d_5 = dice[5]
    if direction == 1:
        dice[0] = d_3; dice[1] = d_1; dice[2] = d_0; dice[3] = d_5; dice[4] = d_4; dice[5] = d_2
    elif direction == 2:
        dice[0] = d_2; dice[1] = d_1; dice[2] = d_5; dice[3] = d_0; dice[4] = d_4; dice[5] = d_3
    elif direction == 3:
        dice[0] = d_4; dice[1] = d_0; dice[2] = d_2; dice[3] = d_3; dice[4] = d_5; dice[5] = d_1
    else:
        dice[0] = d_1; dice[1] = d_5; dice[2] = d_2; dice[3] = d_3; dice[4] = d_0; dice[5] = d_4

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(len(cmd)):
    x += dx[cmd[i] - 1]
    y += dy[cmd[i] - 1]

    if x < 0 or x >= N or y < 0 or y >= M:
        x -= dx[cmd[i] - 1]
        y -= dy[cmd[i] - 1]
        continue
    
    turn(cmd[i])
    if graph[x][y] == 0:
        graph[x][y] = dice[5]
    else:
        dice[5] = graph[x][y]
        graph[x][y] = 0
    print(dice[0])