#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int N, M;
	cin >> N >> M;

	vector<int> basket;
	for (int i = 0; i < N; ++i)
	{
		basket.push_back(i+1);
	}

	for (int m = 0; m < M; ++m)
	{
		int i, j; cin >> i >> j; i--; j--;
		int tmp = basket[i];
		basket[i] = basket[j];
		basket[j] = tmp;
	}

	for (auto it : basket)
	{
		cout << it << " ";
	}
	
	return 0;
}