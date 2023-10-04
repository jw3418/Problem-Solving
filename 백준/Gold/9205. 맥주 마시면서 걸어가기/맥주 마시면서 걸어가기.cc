#include <iostream>
#include <vector>
#include <queue>
using namespace std;

#define MAX 100

int N;
pair<int, int> src;
pair<int, int> mid[MAX];
pair<int, int> dest;
bool visited[MAX];

void bfs(){
    queue<pair<int, int>> Q; Q.push({src.first, src.second});

    while (!Q.empty()){
        int x = Q.front().first; int y = Q.front().second; Q.pop();

        if (abs(x-dest.first)+abs(y-dest.second) <= 1000){
            cout << "happy"; return;
        }
        else{
            for(int i=0; i<N; i++){
                if (!visited[i]){
                    int nx = mid[i].first; int ny = mid[i].second;
                    if (abs(x-nx)+abs(y-ny) <= 1000){
                        Q.push({nx, ny});
                        visited[i] = true;
                    }
                }
            }
        }
    }
    cout << "sad"; return;
}

int main() {
    int T; cin >> T;
    for (int t=0; t<T; t++){
        cin >> N;
        cin >> src.first >> src.second;
        for (int n=0; n<N; n++){
            cin >> mid[n].first >> mid[n].second;
        }
        cin >> dest.first >> dest.second;
        
        for (int i=0; i<MAX; i++){
            visited[i] = false;
        }
        bfs();
        cout << "\n";
    }

    return 0;
}