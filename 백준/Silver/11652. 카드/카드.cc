#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int main()
{
	int N; cin >> N;

	map<long long, long long> Counter;
	for (int i = 0; i < N; ++i)
	{
		long long t; cin >> t;
		Counter[t]++;
	}

	long long max_cnt = 0; long long ans = 0;
	for (auto pair : Counter)
	{
		if (pair.second > max_cnt)
		{
			max_cnt = pair.second;
			ans = pair.first;
		}
	}
	cout << ans;

    return 0;
}
