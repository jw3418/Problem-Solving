#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int N; cin >> N;

	vector<int> vec(N);
	for (int n = 0; n < N; ++n)
	{
		cin >> vec[n];
	}

	int V;
	cin >> V;

	int cnt = 0;
	for (int i = 0; i < N; ++i)
	{
		if (vec[i] == V)
		{
			cnt++;
		}
	}

	cout << cnt;

	return 0;
}