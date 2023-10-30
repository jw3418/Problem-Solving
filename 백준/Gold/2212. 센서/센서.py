import sys

N = int(sys.stdin.readline().strip()); K = int(sys.stdin.readline().strip())
sensor = list(map(int, sys.stdin.readline().strip().split())); sensor.sort()

if K >= N: print(0); exit()

distance = []
for i in range(N-1): distance.append(sensor[i+1] - sensor[i])
distance.sort()

for i in range(K-1): distance.pop() #sensor를 K개의 구간으로 나눠야함 -> 값이 큰 원소 순서대로 K-1개 삭제
print(sum(distance))