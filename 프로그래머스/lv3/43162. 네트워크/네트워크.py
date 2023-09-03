def solution(n, computers):
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        a = find(a); b = find(b)
        if a < b: parent[b] = a
        else: parent[a] = b
        
    parent = [_ for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                if find(i) != find(j): union(i, j)
    
    for i in range(n): find(i) # parent 한 번 갱신 해줘야함
    
    return len(set(parent))