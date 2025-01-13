import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split())) # 0:queue, 1:stack
B = list(map(int, input().split())) # i번 자료구조의 원소
M = int(input())
C = list(map(int, input().split()))

queue = deque([])
for n in range(N):
    if A[n] == 0: queue.append(B[n])

for m in range(M):
    queue.appendleft(C[m])
    print(queue.pop(), end=" ")