#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    vector<int> arr(N + 1);
    for (int i = 1; i <= N; i++) cin >> arr[i];

    vector<vector<bool>> dp(N + 1, vector<bool>(N + 1, false));

    // 길이 1
    for (int i = 1; i <= N; i++) dp[i][i] = true;

    // 길이 2
    for (int i = 1; i < N; i++) {
        if (arr[i] == arr[i + 1]) dp[i][i + 1] = true;
    }

    // 길이 3 이상
    for (int len = 3; len <= N; len++) {
        for (int s = 1; s + len - 1 <= N; s++) {
            int e = s + len - 1;
            if (arr[s] == arr[e] && dp[s + 1][e - 1]) {
                dp[s][e] = true;
            }
        }
    }

    int M;
    cin >> M;
    while (M--) {
        int S, E;
        cin >> S >> E;
        cout << (dp[S][E] ? 1 : 0) << "\n";
    }

    return 0;
}
