import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    heap = []; heapq.heappush(heap, (0, start))
    dists = [int(10e9)] * (N+1); dists[start] = 0

    while heap:
        cur_dist, cur = heapq.heappop(heap)
        if cur_dist < dists[cur]: continue
        for nex, nex_dist in graph[cur]:
            dist = cur_dist + nex_dist
            if dist < dists[nex]:
                dists[nex] = dist
                heapq.heappush(heap, (dist, nex))
    return dists

Z = int(input())
for z in range(Z):
    N, M, T = map(int, input().split())
    S, G, H = map(int, input().split()) #최단경로에 G-H가 포함되어야함

    graph = [[] for n in range(N+1)]; GandH = -1
    for m in range(M):
        a, b, d = map(int, input().split())
        if (a==G and b==H) or (a==H and b==G): GandH = d
        graph[a].append((b, d))
        graph[b].append((a, d))

    zero = dijkstra(S)
    first = dijkstra(G)
    second = dijkstra(H)
    
    ans = []
    for t in range(T):
        x = int(input())
        result = int(10e9)
        gh = zero[G] + GandH + second[x] # S -> G -> H -> T
        hg = zero[H] + GandH + first[x] # S -> H -> G -> T
        if gh == zero[x] or hg == zero[x]: ans.append(x)
    ans.sort(); print(" ".join(map(str, ans)))