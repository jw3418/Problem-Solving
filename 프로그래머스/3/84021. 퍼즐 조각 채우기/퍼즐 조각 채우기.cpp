#include <string>
#include <vector>
#include <deque>
#include <tuple>
#include <set>
#include <algorithm>

using namespace std;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
int N;
vector<vector<bool>> visit;

vector<tuple<int, int>> bfs(int sx, int sy, vector<vector<int>> &board, int color)
{
    visit[sx][sy] = true;
    deque<tuple<int, int>> queue; queue.push_back({sx, sy});
    
    vector<tuple<int, int>> result;
    while (!queue.empty())
    {
        auto [x, y] = queue.front(); queue.pop_front();
        result.push_back({x - sx, y - sy});
        
        for (int i = 0; i < 4; ++i)
        {
            int nx = x + dx[i]; int ny = y + dy[i];
            if (0 <= nx && nx < N && 0 <= ny && ny < N)
            {
                if (board[nx][ny] == color && !visit[nx][ny])
                {
                    visit[nx][ny] = true;
                    queue.push_back({nx, ny});
                }
            }
        }
    }
    
    return result;
}

vector<tuple<int, int>> rotate(vector<tuple<int, int>> src)
{
    vector<tuple<int, int>> des;
    for (auto [x, y] : src)
    {
        des.push_back({y, -x});
    }
    
    return des;
}

vector<tuple<int, int>> normalize(vector<tuple<int, int>> src)
{    
    int min_x = 1e9; int min_y = 1e9;
    for (auto [x, y] : src)
    {
        min_x = min(min_x, x);
        min_y = min(min_y, y);
    }
    for (auto &[x, y] : src)
    {
        x -= min_x;
        y -= min_y;
    }
    
    sort(src.begin(), src.end());
    return src;
}

bool compare_bt(const vector<tuple<int, int>> &src, const vector<tuple<int, int>> &des)
{
    if (src.size() != des.size())
    {
        return false;
    }
    
    for (int i = 0; i < src.size(); ++i)
    {
        if (src[i] != des[i])
        {
            return false;
        }
    }
    return true;
}

int solution(vector<vector<int>> game_board, vector<vector<int>> table) {
    
    N = game_board.size();
    
    vector<vector<tuple<int, int>>> board_result;
    visit = vector<vector<bool>>(N, vector<bool>(N, false));
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            if (game_board[i][j] == 0 && !visit[i][j])
            {
                board_result.push_back(bfs(i, j, game_board, 0));
            }
        }
    }
    
    vector<vector<tuple<int, int>>> table_result;
    visit = vector<vector<bool>>(N, vector<bool>(N, false));
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            if (table[i][j] == 1 && !visit[i][j])
            {
                table_result.push_back(bfs(i, j, table, 1));
            }
        }
    }
    
    int sum_ = 0;
    set<int> visited_idx;
    for (auto &src_shape : board_result)
    {
        src_shape = normalize(src_shape);
        
        for (int i = 0; i < table_result.size(); ++i)
        {
            if (visited_idx.find(i) == visited_idx.end())
            {
                bool break_flag = false;
                vector<tuple<int, int>> des_shape = table_result[i];
                for (int t = 0; t < 4; ++t) // 90도 씩 회전 시키며 비교
                {
                    des_shape = rotate(des_shape);
                    vector<tuple<int, int>> des_shape_normalized = normalize(des_shape);
                    if (compare_bt(src_shape, des_shape_normalized))
                    {
                        sum_ += src_shape.size();
                        break_flag = true;
                        visited_idx.insert(i);
                        break;
                    }                    
                }

                if (break_flag)
                {
                    break;
                }
            }
        }
    }
    
    return sum_;
}