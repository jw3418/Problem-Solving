import sys
from collections import deque
import math

pos = (1, 10, 100, 1000)

def bfs(src, dest):
    queue = deque([])
    queue.append((src, 0)) #수, 횟수
    visit = [False] * 10000
    visit[src] = True

    while queue:
        node, depth = queue.popleft()

        if node == dest:
            return depth

        str_node = str(node)
        for i in range(4):
            for j in range(10):
                nnode = int(str_node[:i] + str(j) + str_node[i+1:])
                if not visit[nnode] and array[nnode] and nnode >= 1000:
                    queue.append((nnode, depth+1))
                    visit[nnode] = True

    return "Impossible"

array = [True for i in range(10000+1)] #소수 배열
for i in range(2, int(math.sqrt(10000)) + 1):
    if array[i] == True:
        j = 2
        while i*j <= 10000:
            array[i*j] = False
            j += 1

T = int(sys.stdin.readline()[:-1])
for _ in range(T):
    src, dest = list(map(int, sys.stdin.readline()[:-1].split()))
    result = bfs(src, dest)
    print(result)