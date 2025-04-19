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

	for (int n = N; n > 0; --n)
	{
		for (int i = 0; i < n; ++i)
		{
			cout << "*";
		}
		cout << endl;
	}

	return 0;
}