import sys
input = sys.stdin.readline

N = int(input()[:-1])
eggs = [] #[내구도, 무게]
for n in range(N): eggs.append(list(map(int, input()[:-1].split())))

def dfs(idx):
    global answer
    if idx == N:
        cnt = 0
        for i in range(N):
            if eggs[i][0] <= 0: cnt += 1
        answer = max(answer, cnt)
        return

    if eggs[idx][0] <= 0: dfs(idx+1)
    else:
        flag = False
        for i in range(N):
            if i == idx: continue
            if eggs[i][0] <= 0: continue
            eggs[idx][0] -= eggs[i][1]; eggs[i][0] -= eggs[idx][1]
            dfs(idx+1); flag = True
            eggs[idx][0] += eggs[i][1]; eggs[i][0] += eggs[idx][1]
        if not flag: dfs(N) #가장 오른쪽에 도달하지 못하고 깰 계란이 없는 경우

answer = 0
dfs(0)
print(answer)