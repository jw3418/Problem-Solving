#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

int main()
{
	int N; cin >> N;

	for (int n = 1; n <= N; ++n)
	{
		for (int i = 1; i <= N; ++i)
		{
			if (i < n)
			{
				cout << " ";
			}
			else
			{
				cout << "*";
			}
		}
		cout << endl;
	}

	return 0;
}