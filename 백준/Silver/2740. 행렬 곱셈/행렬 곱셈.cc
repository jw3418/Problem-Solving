#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <sstream>
#include <numeric>

using namespace std;

int main()
{
	int N, M; cin >> N >> M;
	vector<vector<int>> A;
	for (int n = 0; n < N; ++n)
	{
		vector<int> row;
		for (int m = 0; m < M; ++m)
		{
			int tmp; cin >> tmp;
			row.push_back(tmp);
		}
		A.push_back(row);
	}
	int K; cin >> M >> K;
	vector<vector<int>> B;
	for (int m = 0; m < M; ++m)
	{
		vector<int> row;
		for (int k = 0; k < K; ++k)
		{
			int tmp; cin >> tmp;
			row.push_back(tmp);
		}
		B.push_back(row);
	}

	vector<vector<int>> C(N, vector<int>(K, 0));
	for (int n = 0; n < N; ++n)
	{
		for (int k = 0; k < K; ++k)
		{
			for (int m = 0; m < M; ++m)
			{
				C[n][k] += A[n][m] * B[m][k];
			}
		}
	}

	for (int n = 0; n < N; ++n)
	{
		for (int k = 0; k < K; ++k)
		{
			cout << C[n][k] << " ";
		}
		cout << endl;
	}


	return 0;
}