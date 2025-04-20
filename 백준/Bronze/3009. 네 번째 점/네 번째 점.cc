#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

int main()
{
	map<int, int> counter_x;
	map<int, int> counter_y;
	for (int i = 0; i < 3; ++i)
	{
		int x, y; cin >> x >> y;
		counter_x[x]++;
		counter_y[y]++;
	}

	int X = 0; int Y = 0;
	for (auto pair : counter_x)
	{
		if (pair.second == 1)
		{
			X = pair.first;
		}
	}
	for (auto pair : counter_y)
	{
		if (pair.second == 1)
		{
			Y = pair.first;
		}
	}
	cout << X << " " << Y;
	return 0;
}