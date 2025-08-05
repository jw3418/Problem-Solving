#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    vector<long long> arr(N);
    for (int i = 0; i < N; i++) cin >> arr[i];

    sort(arr.begin(), arr.end());

    long long bestSum = LLONG_MAX;
    vector<long long> result(3);

    for (int i = 0; i < N - 2; i++) {
        int left = i + 1;
        int right = N - 1;

        while (left < right) {
            long long sum = arr[i] + arr[left] + arr[right];

            if (llabs(sum) < llabs(bestSum)) {
                bestSum = sum;
                result = {arr[i], arr[left], arr[right]};
            }

            if (sum > 0) {
                right--;
            } else if (sum < 0) {
                left++;
            } else { 
                // sum == 0 → 최적해
                cout << arr[i] << " " << arr[left] << " " << arr[right] << "\n";
                return 0;
            }
        }
    }

    cout << result[0] << " " << result[1] << " " << result[2] << "\n";
    return 0;
}
