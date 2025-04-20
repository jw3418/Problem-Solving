#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int N, M; cin >> N >> M;
	vector<int> basket(N);
	for (int n = 0; n < N; ++n)
	{
		basket[n] = n+1;
	}

	for (int m = 0; m < M; ++m)
	{
		int S, E; cin >> S >> E; S--; E--;

		vector<int> tmp(E+1 - S);
		for (int i = E; i >= S; --i)
		{
			tmp[E-i] = basket[i];
		}
		for (int i = S; i <= E; ++i)
		{
			basket[i] = tmp[i-S];
		}
	}

	for (int i = 0; i < N; ++i)
	{
		cout << basket[i] << " ";
	}

	return 0;
}