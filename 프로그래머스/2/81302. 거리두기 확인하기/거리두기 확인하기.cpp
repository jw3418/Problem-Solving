#include <string>
#include <vector>
#include <deque>
#include <tuple>

using namespace std;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

vector<int> solution(vector<vector<string>> places) {
    vector<int> answer;
    
    for (auto place : places)
    {
        bool flag = false;
        for (int i = 0; i < 5; ++i)
        {
            for (int j = 0; j < 5; ++j)
            {
                if (place[i][j] == 'P')
                {
                    vector<vector<bool>> visit(5, vector<bool>(5, false)); visit[i][j] = true;
                    deque<tuple<int, int, int>> queue; queue.push_back({i, j, 0});
                    
                    while (!queue.empty())
                    {
                        auto [x, y, cnt] = queue.front(); queue.pop_front();
                        
                        if ((x != i || y != j) && (place[x][y] == 'P' && cnt <= 2))
                        {
                            flag = true;
                            break;
                        }
                        
                        for (int d = 0; d < 4; ++d)
                        {
                            int nx = x + dx[d]; int ny = y + dy[d];
                            if (0 <= nx && nx < 5 && 0 <= ny && ny < 5)
                            {
                                if (!visit[nx][ny] && place[nx][ny] != 'X')
                                {
                                    visit[nx][ny] = true;
                                    queue.push_back({nx, ny, cnt+1});
                                }
                            }
                        }
                    }
                }
                if (flag)
                {
                    break;
                }
            }
            if (flag)
            {
                break;
            }
        }
        if (flag)
        {
            answer.push_back(0);
        }
        else
        {
            answer.push_back(1);
        }
    }
    
    return answer;
}