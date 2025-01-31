import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
P = [0] * (N+1)
for i in range(N): P[i+1] = P[i] + A[i]

R = [0] * M #M으로 나눈 나머지의 개수
for i in range(N): R[P[i+1] % M] += 1

# print(R)
# 같은 나머지를 갖는 누적합끼리의 뺄셈을 통해 구한 구간합은 M으로 나누어 떨어짐!
cnt = R[0] #일단 누적합이 M으로 나누어 떨어지는 경우 더해주고
for i in range(M):
    cnt += R[i] * (R[i]-1) // 2 # 같은 나머지를 갖는 누적합끼리의 뺄셈의 경우의수를 더해줌(nC2)
print(cnt)