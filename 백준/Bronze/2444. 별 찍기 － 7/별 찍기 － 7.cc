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
	for (int n = 1; n < N; ++n)
	{
		for (int i = 1; i <= 2*N; ++i)
		{
			if (i > N - n && i < N+n)
			{
				cout << "*";
			}
			else if (i >= N+n)
			{
				break;
			}
			else
			{
				cout << " ";
			}
		}
		cout << endl;
	}
	for (int i = 1; i < 2*N; ++i)
	{
		cout << "*";
	}
	cout << endl;
	for (int n = N-1; n >= 1; --n)
	{
		for (int i = 1; i <= 2*N; ++i)
		{
			if (i > N - n && i < N+n)
			{
				cout << "*";
			}
			else if (i >= N+n)
			{
				break;
			}
			else
			{
				cout << " ";
			}
		}
		cout << endl;
	}

	return 0;
}