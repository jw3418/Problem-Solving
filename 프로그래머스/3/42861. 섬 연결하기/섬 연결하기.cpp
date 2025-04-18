#include <string>
#include <vector>
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

int solution(int N, vector<vector<int>> costs) {
    
    sort(costs.begin(), costs.end(), [](const vector<int> &a, const vector<int> &b)
         {
             return a[2] < b[2];
         });
    
    for (int i = 0; i < N; ++i)
    {
        parent.push_back(i);
    }
    
    int answer = 0;
    for (auto cost : costs)
    {
        int u = cost[0]; int v = cost[1]; int c = cost[2];
        
        if (Find(u) != Find(v))
        {
            Union(u, v);
            answer += c;
        }
    }
    
    return answer;
}