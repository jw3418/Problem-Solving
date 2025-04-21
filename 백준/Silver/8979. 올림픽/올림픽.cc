#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
	int N, K; cin >> N >> K;

	vector<vector<int>> state;
	for (int i = 0; i < N; ++i)
	{
		int n, g, s, b; cin >> n >> g >> s >> b;
		state.push_back({g, s, b, n});
	}

	sort(state.begin(), state.end(), [](const vector<int> &a, const vector<int> &b)
	{
		if (a[0] != b[0]) return a[0] > b[0];
		if (a[1] != b[1]) return a[1] > b[1];
		return a[2] > b[2];
	});

	int gg = state[0][0], ss = state[0][1], bb = state[0][2];
	int ans = 1;
	for (int i = 0; i < N; ++i)
	{
		if (gg != state[i][0] || ss != state[i][1] || bb != state[i][2])
		{
			gg = state[i][0]; ss = state[i][1]; bb = state[i][2];
			ans = i+1;
		}
		if (state[i][3] == K)
		{
			cout << ans;
			break;
		}
	}

	return 0;
}