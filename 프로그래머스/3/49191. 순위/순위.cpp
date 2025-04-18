#include <string>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <iostream>

using namespace std;

int N;

void bfs(int start, map<int, vector<int>> &graph, map<int, set<int>> &nodes)
{
    vector<bool> visit(N+1, false); visit[start] = true;
    deque<int> queue; queue.push_back(start);
    
    while (!queue.empty())
    {
        int cur = queue.front(); queue.pop_front();
        nodes[cur].insert(cur);
        
        for (auto nex : graph[cur])
        {
            if (!visit[nex])
            {
                visit[nex] = true;
                queue.push_back(nex);
                
                for (auto it : nodes[cur])
                {
                    nodes[nex].insert(it);
                }
            }
        }
        
    }
    
}

int solution(int n, vector<vector<int>> results) {
    
    N = n;
    
    map<int, vector<int>> win_graph;
    map<int, vector<int>> lose_graph;
    for (auto result : results)
    {
        win_graph[result[0]].push_back(result[1]);
        lose_graph[result[1]].push_back(result[0]);
    }
    
    map<int, set<int>> win_nodes;   //bfs 탐색하면서 접근 가능한 모든 nodes들을 모음
    map<int, set<int>> lose_nodes;  //bfs 탐색하면서 접근 가능한 모든 nodes들을 모음
    for (int i = 1; i <= N; ++i)
    {
        bfs(i, win_graph, win_nodes);
        bfs(i, lose_graph, lose_nodes);
    }
    
    int ans = 0;
    for (int i = 1; i <= N; ++i)
    {
        // cout << win_nodes[i].size() << ", " << lose_nodes[i].size() << endl;
        if (win_nodes[i].size() + lose_nodes[i].size() == N+1)
        {
            ans++;
        }
    }
    
    return ans;
}