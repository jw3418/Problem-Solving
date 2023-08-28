import sys

N, L = map(int, input().split())
Map = []; Road = []
for n in range(N):
    tmp = list(map(int, sys.stdin.readline()[:-1].split()))
    Map.append(tmp)
    Road.append(tmp)
for i in range(N):
    tmp = []
    for j in range(N):
        tmp.append(Map[j][i])
    Road.append(tmp)

result = 0
for i in range(2 * N):
    tmp_result = True; setted = [False for _ in range(N)]; escape = False
    for j in range(1, N):
        if abs(Road[i][j] - Road[i][j-1]) > 1: #2칸 이상 높아지거나 낮아진 경우
            tmp_result = False; break
        elif Road[i][j-1] - Road[i][j] == 1: #1칸 낮아진 경우 -> 오른쪽 탐색
            for k in range(L):
                if j+k >= N or setted[j+k] or Road[i][j] != Road[i][j+k]:
                    tmp_result = False; escape = True; break
                if Road[i][j] == Road[i][j+k]:
                    setted[j+k] = True
            if escape:
                break
        elif Road[i][j] - Road[i][j-1] == 1: #1칸 높아진 경우 -> 왼쪽 탐색
            for k in range(L):
                if j-k-1 < 0 or setted[j-k-1] or Road[i][j-1] != Road[i][j-k-1]:
                    tmp_result = False; escape = True; break
                if Road[i][j-1] == Road[i][j-k-1]:
                    setted[j-k-1] = True
            if escape:
                break

    if tmp_result:
        result += 1

print(result)