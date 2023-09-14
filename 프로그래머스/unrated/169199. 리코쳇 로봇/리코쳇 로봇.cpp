#include <string>
#include <vector>
#include <queue>
#include <limits.h>
#define MAX 100

using namespace std;

int N, M;
int answer = INT_MAX;
pair<int, int> start;
pair<int, int> goal;
bool visited[MAX][MAX]; // 전역변수 초기화 -> False

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void bfs(vector<string> &board) {
    queue<pair<pair<int, int>, int>> q;
    q.push({{start.first, start.second}, 0});
    visited[start.first][start.second] = true;
    
    while (!q.empty()) {
        int x = q.front().first.first;
        int y = q.front().first.second;
        int depth = q.front().second;
        q.pop();
        
        if (x == goal.first && y == goal.second) {
            answer = min(answer, depth);
        }
        
        for (int i=0; i<4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (0 <= nx && nx < N && 0 <= ny && ny < M){
                if (board[nx][ny] != 'D'){
                    while (true) {
                        nx += dx[i];
                        ny += dy[i];
                    
                        if ((nx < 0 || N <= nx || ny < 0 || M <= ny) || board[nx][ny] == 'D') {
                            nx -= dx[i];
                            ny -= dy[i];
                            break;
                        }
                    }
           
                    if (visited[nx][ny]) continue;
            
                    q.push({{nx, ny}, depth + 1});
                    visited[nx][ny] = true;
                }
            }
        }
    }
}

int solution(vector<string> board) {
    N = board.size();
    M = board[0].size();
    
    int cnt = 0;
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            if (cnt == 2) break;
            
            if (board[i][j] == 'R') {
                cnt++;
                start = {i, j};
            } else if (board[i][j] == 'G') {
                cnt++;
                goal = {i, j};
            }
        }
    }
    
    bfs(board);
    
    if (answer == INT_MAX) return -1;
    return answer;
}
