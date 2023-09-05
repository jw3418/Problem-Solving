def solution(n, wires):
    N = len(wires)
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        a = find(a); b = find(b)
        if a < b: parent[b] = a
        else: parent[a] = b
            
    diff = []
    for i in range(N):
        parent = [_ for _ in range(n+1)]
        for j in range(N):
            if i == j: continue
            union(wires[j][0], wires[j][1])
        
        for j in range(1, n+1): find(j)
        
        parent_nodes = list(set(parent[1:]))
        diff.append(abs(parent.count(parent_nodes[0]) - parent.count(parent_nodes[1])))
        
    return min(diff)