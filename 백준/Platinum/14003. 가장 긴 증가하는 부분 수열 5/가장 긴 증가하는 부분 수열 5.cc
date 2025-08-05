#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;

    vector<int> A(N), lis;      // LIS 배열
    vector<int> pos(N);         // 각 원소의 LIS 위치 기록

    for (int i = 0; i < N; i++) cin >> A[i];

    for (int i = 0; i < N; i++) {
        auto it = lower_bound(lis.begin(), lis.end(), A[i]);
        int idx = it - lis.begin();

        if (it == lis.end()) lis.push_back(A[i]);
        else *it = A[i];

        pos[i] = idx;  // A[i]는 LIS 내 idx 위치
    }

    // LIS 복원
    int length = lis.size();
    vector<int> result(length);

    for (int i = N - 1; i >= 0; i--) {
        if (pos[i] == length - 1) {
            result[--length] = A[i];
        }
    }

    cout << lis.size() << "\n";
    for (int v : result) cout << v << " ";
    cout << "\n";

    return 0;
}
