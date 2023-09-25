#include <iostream>
#include <vector>
#include <queue>
#include <limits.h>
using namespace std;

#define INF INT_MAX
#define MAX 125

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int N, cnt;
int graph[MAX][MAX];
int costs[MAX][MAX];

void dijkstra(){
    priority_queue<pair<int, pair<int, int> > > PQ;
    PQ.push(make_pair(-graph[0][0], make_pair(0, 0)));
    costs[0][0] = 0;

    while (!PQ.empty()){
        int cost = -PQ.top().first;
        int x = PQ.top().second.first;
        int y = PQ.top().second.second;
        PQ.pop();

        if (x == N-1 && y == N-1){
            cout << "Problem " << cnt << ": " << cost << '\n';
            break;
        }

        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < N && 0 <= ny && ny < N){
                int ncost = cost + graph[nx][ny];
                if (costs[nx][ny] > ncost){
                    costs[nx][ny] = ncost;
                    PQ.push(make_pair(-costs[nx][ny], make_pair(nx, ny)));
                }
            }
        }
    }
}

int main() {
    cnt = 0;
    while(true){
        cin >> N;
        if (N == 0){
            break;
        }

        cnt++;
        for (int i=0; i<N; i++){
            for (int j=0; j<N; j++){
                costs[i][j] = INF;
                cin >> graph[i][j];
            }
        }

        dijkstra();
    }

    return 0;
}