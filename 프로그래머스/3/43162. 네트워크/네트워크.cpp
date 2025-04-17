#include <string>
#include <vector>
#include <iostream>
#include <set>

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

int solution(int N, vector<vector<int>> computers) {
    
    for (int i = 0; i < N; ++i)
    {
        parent.push_back(i);
    }
    
    for (int i = 0; i < N; ++i)
    {
        for (int j = i+1; j < N; ++j)
        {
            if (computers[i][j] == 1)
            {
                if (Find(i) != Find(j))
                {
                    Union(i, j);
                }
            }
        }
    }
    
    for (int i = 0; i < N; ++i)
    {
        Find(i);
    }
    
    
    set<int> parent_set(parent.begin(), parent.end());
    
    return parent_set.size();
}