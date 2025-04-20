#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>

using namespace std;

int main()
{
	int N; cin >> N;
	
	vector<int> dp(N+1, 0);
	dp[1] = 1;

	for (int i = 2; i <= N; ++i)
	{
		dp[i] = dp[i-1] + dp[i-2];
	}

	cout << dp[N];
	return 0;
}