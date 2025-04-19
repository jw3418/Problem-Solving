#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

int main()
{
	int T; cin >> T;
	for (int t = 0; t < T; ++t)
	{
		int K, N; cin >> K; cin >> N;

		vector<int> floor(N, 0);
		for (int i = 0; i < N; ++i)
		{
			floor[i] = i+1;
		}

		for (int k = 1; k <= K; ++k)
		{
			int tmp = 0;
			for (int i = 0; i < N; ++i)
			{
				tmp += floor[i];
				floor[i] = tmp;
			}
		}
		cout << floor[N-1] << endl;
	}

	return 0;
}