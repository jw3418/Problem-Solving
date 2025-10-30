import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find_articulation_points():
    # 입력 받기
    V, E = map(int, input().split())
    
    # 그래프 인접 리스트로 저장
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    # 필요한 변수들 초기화
    visited = [False] * (V + 1)  # 방문 여부
    visit_order = [0] * (V + 1)  # DFS 방문 순서 
    low = [0] * (V + 1)          # 해당 정점에서 갈 수 있는 가장 빠른 방문 순서
    parent = [-1] * (V + 1)      # DFS 트리에서의 부모
    articulation_points = set()  # 단절점들을 저장
    order_counter = [1]          # 방문 순서 카운터 (전역 변수 역할)
    
    def dfs(cur):
        # 현재 정점 방문 처리
        visited[cur] = True
        visit_order[cur] = low[cur] = order_counter[0]
        order_counter[0] += 1
        
        children = 0  # 자식 노드 개수 (루트 노드의 단절점 판별용)
        
        # 인접한 모든 정점 탐색
        for nex in graph[cur]:
            if not visited[nex]:  # 아직 방문하지 않은 정점 (트리 간선)
                children += 1
                parent[nex] = cur
                dfs(nex)
                
                # 자식에서 돌아왔을 때 low 값 갱신
                low[cur] = min(low[cur], low[nex])
                
                # 단절점 판별 조건 1: 루트 노드이면서 자식이 2개 이상
                if parent[cur] == -1 and children > 1:
                    articulation_points.add(cur)
                
                # 단절점 판별 조건 2: 루트가 아닌 노드에서 
                # 자식이 현재 노드보다 이전 또는 같은 시점에만 갈 수 있음
                if parent[cur] != -1 and low[nex] >= visit_order[cur]:
                    articulation_points.add(cur)
                    
            elif nex != parent[cur]:  # 이미 방문했지만 부모가 아닌 경우 (역방향 간선)
                # 역방향 간선이므로 low 값 갱신
                low[cur] = min(low[cur], visit_order[nex])
    
    # 모든 연결 요소에 대해 DFS 실행 (연결 그래프가 아닐 수도 있음)
    for i in range(1, V + 1):
        if not visited[i]:
            dfs(i)
    
    # 결과 출력
    result = sorted(list(articulation_points))
    print(len(result))
    if result:
        print(*result)
    else:
        print()

# 실행
find_articulation_points()