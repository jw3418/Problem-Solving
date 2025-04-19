#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int N, M;
	cin >> N >> M;

	vector<vector<int>> vec;
	for (int i = 0; i < N; ++i)
	{
		vector<int> tmp;
		for (int j = 0; j < M; ++j)
		{
			int t; cin >> t;
			tmp.push_back(t);
		}
		vec.push_back(tmp);
	}
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < M; ++j)
		{
			int t; cin >> t;
			vec[i][j] += t; 
		}
	}

	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < M; ++j)
		{
			cout << vec[i][j] << " ";
		}
		cout << endl;
	}

	return 0;
}