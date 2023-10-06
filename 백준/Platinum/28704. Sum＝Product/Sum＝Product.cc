#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int N;
    cin >> N;
    int64_t tot_sum = 0;
    vector<int> A(N + 2, -1);
    for (int i = 1; i <= N; i++)
        cin >> A[i], tot_sum += A[i];

    vector<int> I;
    for (int i = 0; i <= N + 1; i++)
        if (A[i] != 1)
            I.push_back(i);

    int64_t ans = N;
    int K = I.size() - 2;
    for (int L = 1; L <= K; L++)
    {
        int64_t mul = 1, sum = 0;
        for (int R = L; R <= K; R++)
        {
            mul *= A[I[R]];
            sum += A[I[R]] - 1;
            if (mul > tot_sum)
                break;
            if (L != R)
            {
                int64_t U = I[L] - I[L - 1] - 1;
                int64_t V = I[R + 1] - I[R] - 1;
                int64_t Z = mul - (sum + I[R] - I[L] + 1);
                if (0 <= Z && Z <= U + V)
                    ans += min({Z, U + V - Z, U, V}) + 1;
            }
        }
    }
    cout << ans << endl;
}
