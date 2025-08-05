#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;

    vector<int> r(N + 1), c(N + 1);
    for (int i = 1; i <= N; i++) {
        cin >> r[i] >> c[i];
    }

    vector<vector<long long>> dp(N + 1, vector<long long>(N + 1, 0));

    for (int len = 2; len <= N; len++) {         // 구간 길이
        for (int i = 1; i + len - 1 <= N; i++) {
            int j = i + len - 1;
            dp[i][j] = LLONG_MAX;

            for (int k = i; k < j; k++) {
                long long cost = dp[i][k] + dp[k + 1][j] + 1LL * r[i] * c[k] * c[j];
                dp[i][j] = min(dp[i][j], cost);
            }
        }
    }

    cout << dp[1][N] << "\n";
    return 0;
}
