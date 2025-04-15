#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

vector<int> parent;

int Find(int x)
{
    if (parent[x] != x)
    {
        parent[x] = Find(parent[x]);
    }
    return parent[x];
}

void Union(int a, int b)
{
    a = Find(a); b = Find(b);
    if (a < b)
    {
        parent[b] = a;
    }
    else
    {
        parent[a] = b;
    }
}

int solution(int n, vector<vector<int>> wires) {
    
    vector<int> diff;
    for (int i = 0; i < wires.size(); ++i)
    {
        parent.clear();
        for (int j = 0; j <= n; ++j)
        {
            parent.push_back(j);
        }
        
        for (int j = 0; j < wires.size(); ++j)
        {
            if (i == j)
            {
                continue;
            }
            Union(wires[j][0], wires[j][1]);
        }
        
        for (int j = 1; j <= n; ++j)
        {
            Find(j);
        }
        
        set<int> parent_nodes_set(parent.begin() + 1, parent.end());
        vector<int> parent_nodes_vec(parent_nodes_set.begin(), parent_nodes_set.end());
        
        diff.push_back(abs(count(parent.begin(), parent.end(), parent_nodes_vec[0]) - count(parent.begin(), parent.end(), parent_nodes_vec[1])));
    }
    
    return *min_element(diff.begin(), diff.end());
}