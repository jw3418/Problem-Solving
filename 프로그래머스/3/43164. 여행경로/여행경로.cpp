#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<vector<string>> path_results;
int N;
vector<bool> visit;

void dfs(string cur, vector<string> path, vector<vector<string>> &tickets)
{
    if (path.size() == N+1)
    {
        path_results.push_back(path);
        return;
    }
    else
    {
        for (int i = 0; i < N; ++i)
        {
            if (!visit[i] && tickets[i][0] == cur)
            {
                visit[i] = true; path.push_back(tickets[i][1]);
                dfs(tickets[i][1], path, tickets);
                visit[i] = false; path.pop_back();
            }
        }
    }
}

vector<string> solution(vector<vector<string>> tickets) {
    
    N = tickets.size();

    sort(tickets.begin(), tickets.end());
    visit.resize(N, false);
    dfs("ICN", {"ICN"}, tickets);
    
    return path_results[0];
}