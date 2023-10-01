#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <array>
using namespace std;

#define MAX 100

int A, B, N, M;
int board[MAX][MAX] = {0, };
map<int, vector<int> > robot;
map<char, int> direction;

//NWES
int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

int main() {
    cin >> A >> B;    
    cin >> N >> M;
    direction['N'] = 0; direction['W'] = 1; direction['E'] = 2; direction['S'] = 3;

    for (int n=1; n<=N; n++){
        int x, y;
        char d;
        cin >> y >> x >> d;
        x = B - x; y--;
        board[x][y] = n; robot[n] = vector<int> {x, y, direction[d]};
    }
    
    for (int m=0; m<M; m++){
        int num, iteration;
        char cmd;
        cin >> num >> cmd >> iteration;
        if (cmd == 'L'){
            iteration %= 4;
            for (int t=0; t<iteration; t++){
                int d = robot[num][2];
                if (d == 0) robot[num][2] = 1;
                else if (d == 1) robot[num][2] = 3;
                else if (d == 2) robot[num][2] = 0;
                else if (d == 3) robot[num][2] = 2;
            }
        }
        else if (cmd == 'R'){
            iteration %= 4;
            for (int t=0; t<iteration; t++){
                int d = robot[num][2];
                if (d == 0) robot[num][2] = 2;
                else if (d == 1) robot[num][2] = 0;
                else if (d == 2) robot[num][2] = 3;
                else if (d == 3) robot[num][2] = 1;
            }
        }
        else if (cmd == 'F'){
            for (int t=0; t<iteration; t++){
                int x = robot[num][0]; int y = robot[num][1]; int d = robot[num][2];
                int nx = x + dx[d]; int ny = y + dy[d];
                if (0 <= nx && nx < B && 0 <= ny && ny < A){
                    if (board[nx][ny] != 0){
                        cout << "Robot " << num << " crashes into robot " << board[nx][ny] << endl;
                        return 0;
                    }
                    else{
                        board[x][y] = 0; board[nx][ny] = num;
                        robot[num] = vector<int> {nx, ny, d};
                    }
                }
                else{
                    cout << "Robot " << num << " crashes into the wall" << endl;
                    return 0;
                }
            }
        }
    }
    cout << "OK" << endl;

    return 0;
}