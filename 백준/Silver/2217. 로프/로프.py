import sys

N = int(sys.stdin.readline().strip())
ropes = [int(sys.stdin.readline().strip()) for n in range(N)]; ropes.sort(reverse=True)

weights = []
for i in range(N): weights.append(ropes[i] * (i+1))
print(max(weights))