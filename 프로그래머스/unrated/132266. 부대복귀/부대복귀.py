from collections import deque

def solution(n, roads, sources, destination):
    
    edges = dict()
    for road in roads:
        if road[0] in edges: edges[road[0]].append(road[1])
        else: edges[road[0]] = [road[1]]
        if road[1] in edges: edges[road[1]].append(road[0])
        else: edges[road[1]] = [road[0]]
    
    queue = deque([]); queue.append((destination, 0))
    visit = set(); visit.add(destination)
    
    sources_set = set(sources); result = dict()
    while queue:
        node, cnt = queue.popleft()
        
        if node in sources_set: result[node] = cnt
        
        for nnode in edges[node]:
            if nnode not in visit:
                visit.add(nnode); queue.append((nnode, cnt+1))
    
    answer = []
    for source in sources:
        if source in result: answer.append(result[source])
        else: answer.append(-1)
    return answer