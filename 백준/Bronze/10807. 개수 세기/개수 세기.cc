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

	int cnt = count(vec.begin(), vec.end(), V);
	cout << cnt;

	return 0;
}