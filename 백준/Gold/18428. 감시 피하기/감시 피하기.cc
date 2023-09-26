#include <iostream>
#include <vector>
#include <queue>
#include <limits.h>
using namespace std;

#define INF INT_MAX
#define MAX 6

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int N;
char board[MAX][MAX];
bool answer = false;
vector<pair<int, int> > teachers;

bool check(){
    queue<pair<int, int> > q;
    for (int i=0; i<teachers.size(); i++){
        q.push(make_pair(teachers[i].first, teachers[i].second));
    }
    
    while (!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            while (0 <= nx && nx < N && 0 <= ny && ny < N){
                if (board[nx][ny] == 'S'){
                    return false;
                }
                else if (board[nx][ny] == 'T' || board[nx][ny] == 'O'){
                    break;
                }
                nx += dx[i];
                ny += dy[i];
            }
        }
    }
    return true;
}

void backtracking(int o_cnt){
    if (o_cnt == 3){
        if (check()){
            answer = true;
            return;
        }
    }
    else{
        for (int i=0; i<N; i++){
            for (int j=0; j<N; j++){
                if (board[i][j] == 'X'){
                    board[i][j] = 'O';
                    backtracking(o_cnt+1);
                    board[i][j] = 'X';
                }
            }
        }
    }
}

int main() {
    cin >> N;

    for (int i=0; i<N; i++){
        for (int j=0; j<N; j++){
            cin >> board[i][j];
            if (board[i][j] == 'T'){
                teachers.push_back(make_pair(i, j));
            }
        }
    }

    backtracking(0);
    if (answer) {
        cout << "YES\n";
    }
    else{
        cout << "NO\n";
    }

    return 0;
}