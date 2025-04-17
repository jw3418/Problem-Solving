#include <vector>
#include <deque>
#include <tuple>

using namespace std;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int solution(vector<vector<int>> maps)
{
    int N = maps.size(); int M = maps[0].size();
    
    deque<tuple<int, int, int>> queue; queue.push_back({0, 0, 1});
    vector<vector<bool>> visit(N, vector<bool>(M, false)); visit[0][0] = true;
    
    int ans = -1;
    while (!queue.empty())
    {
        auto [x, y, cnt] = queue.front(); queue.pop_front();
        
        if (x == N-1 && y == M-1)
        {
            ans = cnt;
            break;
        }
        
        for (int i = 0; i < 4; ++i)
        {
            int nx = x + dx[i]; int ny = y + dy[i];
            if (0 <= nx && nx < N && 0 <= ny && ny < M)
            {
                if (maps[nx][ny] == 1 && !visit[nx][ny])
                {
                    queue.push_back({nx, ny, cnt+1});
                    visit[nx][ny] = true;
                }
            }
        }
    }

    return ans;
}