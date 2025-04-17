#include <string>
#include <vector>
#include <deque>
#include <tuple>

using namespace std;

int solution(vector<vector<int>> rectangle, int characterX, int characterY, int itemX, int itemY) {
    
    int dx[4] = {0, 0, -1, 1};
    int dy[4] = {-1, 1, 0, 0};
    
    characterX *= 2; characterY *= 2; itemX *= 2; itemY *= 2;
    vector<vector<bool>> board(51*2, vector<bool>(51*2, false));
    
    for (auto rec: rectangle)
    {
        for (int x = rec[0]*2; x <= rec[2]*2; ++x)
        {
            for (int y = rec[1]*2; y <= rec[3]*2; ++y)
            {
                board[x][y] = true;
            }
        }
    }
    
    for (auto rec: rectangle)
    {
        for (int x = rec[0]*2+1; x < rec[2]*2; ++x)
        {
            for (int y = rec[1]*2+1; y < rec[3]*2; ++y)
            {
                board[x][y] = false;
            }
        }
    }
    
    deque<tuple<int, int, int>> queue; queue.push_back({characterX, characterY, 0});
    vector<vector<bool>> visit(51*2, vector<bool>(51*2, false)); visit[characterX][characterY] = true;
    
    while (!queue.empty())
    {
        auto [x, y, cnt] = queue.front(); queue.pop_front();
        
        if (x == itemX && y == itemY)
        {
            return cnt / 2;
        }
        
        for (int i = 0; i < 4; ++i)
        {
            int nx = x + dx[i]; int ny = y + dy[i];
            if (0 <= nx && nx < 51*2 && 0 <= ny && ny < 51*2)
            {
                if (!visit[nx][ny] && board[nx][ny])
                {
                    visit[nx][ny] = true;
                    queue.push_back({nx, ny, cnt+1});
                }
            }
        }
    }
    
    return 0;
}