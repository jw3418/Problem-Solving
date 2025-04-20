#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <sstream>

using namespace std;

int main()
{
	int x, y; cin >> x >> y;

	vector<int> days = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	int sum_ = 0;
	for (int i = 1; i < x; ++i)
	{
		sum_ += days[i];
	}
	sum_ += y;

	int mod = sum_ % 7;
	if (mod == 0)
	{
		cout << "SUN";
	}
	else if (mod == 1)
	{
		cout << "MON";
	}
	else if (mod == 2)
	{
		cout << "TUE";
	}
	else if (mod == 3)
	{
		cout << "WED";
	}
	else if (mod == 4)
	{
		cout << "THU";
	}
	else if (mod == 5)
	{
		cout << "FRI";
	}
	else if (mod == 6)
	{
		cout << "SAT";
	}

	return 0;
}