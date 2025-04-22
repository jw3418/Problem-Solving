#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int main()
{
	int N; cin >> N;
	vector<int> ticket;
	for (int i = 0; i < N; ++i)
	{
		int t; cin >> t;
		ticket.push_back(t);
	}

	vector<int> pos(N);
	for (int i = 0; i < N; ++i)
	{
		pos[i] = i;
	}
	for (int i = 0; i < N; ++i)
	{
		int step = ticket[i];
		for (int s = 0; s < N; ++s)
		{
			if (pos[s] >= i-step && pos[s] <= i-1)
			{
				pos[s]++;
			}
		}
		pos[i] = i-step;
	}

	vector<int> ans(N);
	for (int i = 0; i < N; ++i)
	{
		ans[pos[i]] = i+1;
	}
	for (int i = 0; i < N; ++i)
	{
		cout << ans[i] << " ";
	}
	cout << endl;

    return 0;
}
