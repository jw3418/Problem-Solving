import sys

#위치 당 점수
board_score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18,
            20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
            40, 13, 16, 19, 25, 22, 24, 28, 27, 26,
            30, 35, 0]
graph = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], [12], [13], [14], [15], [16, 27], [17], [18], [19], [20], [32], [22], [23], [24], [30], [26], [24], [28], [29], [24], [31], [20], [32]]

def backtracking(idx, score, horse):
    global max_score

    if idx == len(dice):
        max_score = max(max_score, score)
        return
    
    for i in range(len(horse)):
        curr = horse[i]

        ##### 주사위 수만큼 말 이동
        if len(graph[curr]) == 2:
            next = graph[curr][1]
        else:
            next = graph[curr][0]
        for j in range(dice[idx] - 1):
            next = graph[next][0]

        ##### 가능한 경우인지 확인하고, 가능하다면 진행
        if next == 32 or next not in horse:
            horse[i] = next
            backtracking(idx+1, score + board_score[next], horse)
            horse[i] = curr #for backtracking


dice = list(map(int, sys.stdin.readline()[:-1].split())) #주사위의 수

max_score = 0
backtracking(0, 0, [0, 0, 0, 0])
print(max_score)