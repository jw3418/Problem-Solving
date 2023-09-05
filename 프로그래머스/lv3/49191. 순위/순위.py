from collections import deque

def solution(n, results):
    
    def bfs(start, graph, individual_nodes):
        queue = deque([]); queue.append(start)
        visit = [False] * (n+1); visit[start] = True
        
        while queue:
            curr = queue.popleft()
            individual_nodes[curr].add(curr)
            
            if curr not in graph: continue
            
            for element in graph[curr]:
                if not visit[element]:
                    visit[element] = True
                    queue.append(element)
                    for c in individual_nodes[curr]:
                        individual_nodes[element].add(c)
        
    
    win_graph = dict(); lose_graph = dict()
    for result in results:
        w, l = result
        if w in win_graph: win_graph[w].append(l)
        else: win_graph[w] = [l]
        if l in lose_graph: lose_graph[l].append(w)
        else: lose_graph[l] = [w]
    
    win_nodes = dict(); lose_nodes = dict()
    for i in range(1, n+1):
        win_nodes[i] = set(); lose_nodes[i] = set()
    
    for i in range(1, n+1):
        bfs(i, win_graph, win_nodes)
        bfs(i, lose_graph, lose_nodes)
    
    answer = 0
    for i in range(1, n+1):
        if len(win_nodes[i]) + len(lose_nodes[i]) == n+1: answer += 1
    return answer