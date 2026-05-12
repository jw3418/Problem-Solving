import heapq

def solution(N, road, K):
    graph = dict()
    for a, b, c in road:
        if a in graph: graph[a].append((b, c))
        else: graph[a] = [(b, c)]
        if b in graph: graph[b].append((a, c))
        else: graph[b] = [(a, c)]
        
    distance = [int(10e9) for _ in range(N+1)]; distance[1] = 0
    
    heap = [(0, 1)]
    while heap:
        cdist, cnode = heapq.heappop(heap)
        if cdist > distance[cnode]: continue
            
        for nnode, dist in graph[cnode]:
            ndist = cdist + dist
            
            if ndist < distance[nnode]:
                distance[nnode] = ndist
                heapq.heappush(heap, (ndist, nnode))
    
    cnt = 1
    for i in range(2, N+1):
        if distance[i] <= K:
            cnt += 1        
    return cnt