#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
int N;
int W[16][16];
int dp[16][1 << 16];

int tsp(int cur, int visited) {
    if (visited == (1 << N) - 1) {
        return W[cur][0] ? W[cur][0] : INF;  // 모든 도시 방문 후 출발점으로 복귀
    }
    
    int &ret = dp[cur][visited];
    if (ret != -1) return ret;
    
    ret = INF;
    for (int next = 0; next < N; ++next) {
        if (!(visited & (1 << next)) && W[cur][next] > 0) {
            ret = min(ret, tsp(next, visited | (1 << next)) + W[cur][next]);
        }
    }
    return ret;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> W[i][j];
        }
    }

    memset(dp, -1, sizeof(dp));
    cout << tsp(0, 1) << "\n";
    return 0;
}
