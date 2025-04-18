#include <string>
#include <vector>
#include <map>
#include <deque>
#include <tuple>
#include <iostream>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    
    map<int, vector<int>> adj;
    for (int i = 0; i < edge.size(); ++i)
    {
        adj[edge[i][0]].push_back(edge[i][1]);
        adj[edge[i][1]].push_back(edge[i][0]);
    }
        
    deque<tuple<int, int>> queue; queue.push_back({1, 0});
    vector<bool> visit(n+1, false); visit[1] = true;
    
    int max_depth = 0; vector<int> result;
    while (!queue.empty())
    {
        auto [cur, depth] = queue.front(); queue.pop_front();
        if (max_depth < depth)
        {
            max_depth = depth;
            result.clear();
        }
        result.push_back(cur);
                
        for (auto nex : adj[cur])
        {
            if (!visit[nex])
            {
                visit[nex] = true;
                queue.push_back({nex, depth+1});
            }
        }
    }
        
    return result.size();
}