#include <string>
#include <vector>
#include <iostream>
#include <limits.h>
#include <queue>
#define MAX 100
using namespace std;

int N, M;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int bfs(vector<string> &maps, pair<int, int> start, pair<int, int> end){
    queue<pair<pair<int, int>, int>> queue;
    queue.push({{start.first, start.second}, 0});
    
    int visit[MAX][MAX] = {false,};
    visit[start.first][start.second] = true;
    
    while (!queue.empty()){
        int x = queue.front().first.first;
        int y = queue.front().first.second;
        int depth = queue.front().second;
        queue.pop();
        
        if (x == end.first && y == end.second){
            return depth;
        }
        
        for (int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (0 <= nx && nx < N && 0 <= ny && ny < M){
                if (maps[nx][ny] != 'X' && visit[nx][ny] == false){
                    queue.push({{nx, ny}, depth+1});
                    visit[nx][ny] = true;
                }
            }
        }
    }
    return -1;
}

int solution(vector<string> maps) {
    N = maps.size();
    M = maps[0].length();
    
    pair<int, int> S, E, L;
    for (int i=0; i<N; i++){
        for (int j=0; j<M; j++){
            if (maps[i][j] == 'S'){
                S = {i, j};
            }
            else if (maps[i][j] == 'E'){
                E = {i, j};
            }
            else if (maps[i][j] == 'L'){
                L = {i, j};
            }
        }
    }
    
    int pre_count = bfs(maps, S, L);
    if (pre_count == -1) return -1;
    int post_count = bfs(maps, L, E);
    if (post_count == -1) return -1;
    return pre_count+post_count;
}