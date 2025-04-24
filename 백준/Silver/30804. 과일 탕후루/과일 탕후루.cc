#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <string>

using namespace std;

int main()
{
	int N; cin >> N;
	vector<int> S(N);
	for (int i = 0; i < N; ++i)
	{
		cin >> S[i];
	}

	int l = 0; int r = 0;
	int ans = 0;
	unordered_map<int, int> Counter;
	while (r < N)
	{
		Counter[S[r]]++;

		while (Counter.size() > 2)
		{
			Counter[S[l]]--;
			if (Counter[S[l]] == 0)
			{
				Counter.erase(S[l]);
			}
			l++;
		}

		ans = max(ans, r - l + 1);
		r++;
	}
	cout << ans << endl;

    return 0;
}
