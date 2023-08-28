import sys


def solution(x, y, d1, d2):
    global total_poplutaion
    population = [0, 0, 0, 0, 0]

    #1번 선거구
    for r in range(0, x+d1):
        for c in range(0, y+1):
            if area[r][c] == 5:
                break 
            population[0] += board[r][c]

    #2번 선거구
    for r in range(0, x+d2+1):
        for c in range(N-1, y, -1):
            if area[r][c] == 5:
                break
            population[1] += board[r][c]

    #3번 선거구
    for r in range(x+d1, N):
        for c in range(0, y-d1+d2):
            if area[r][c] == 5:
                break
            population[2] += board[r][c]

    #4번 선거구
    for r in range(x+d2+1, N):
        for c in range(N-1, y-d1+d2-1, -1):
            if area[r][c] == 5:
                break
            population[3] += board[r][c]

    #5번 선거구
    population[4] = total_poplutaion - sum(population)

    return abs(max(population) - min(population))


N = int(sys.stdin.readline()[:-1])
board = []; total_poplutaion = 0
for n in range(N):
    tmp = list(map(int, sys.stdin.readline()[:-1].split()))
    total_poplutaion += sum(tmp)
    board.append(tmp)

result = 10e9
for x in range(N):
    for y in range(N):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if x+d1+d2 > N-1 or y-d1 <0 or y+d2 > N-1:
                    continue
                # 경계선 그리기
                area = [[0] * N for _ in range(N)]
                area[x][y] = 5
                for i in range(1, d1+1):
                    area[x+i][y-i] = 5
                for i in range(1, d2+1):
                    area[x+i][y+i] = 5
                for i in range(1, d2+1):
                    area[x+d1+i][y-d1+i] = 5
                for i in range(1, d1+1):
                    area[x+d2+i][y+d2-i] = 5

                # for t in range(N):
                #     print(area[t])
                # print(solution(x, y, d1, d2))
                # print()
                result = min(result, solution(x, y, d1, d2))
                    
print(result)