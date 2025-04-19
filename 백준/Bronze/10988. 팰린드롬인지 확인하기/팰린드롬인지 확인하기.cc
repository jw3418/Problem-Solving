#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	string str; cin >> str;
	int N = str.length();

	vector<char> stack;
	if (N%2 == 0)
	{
		for (int i = 0; i < (int)N/2; ++i)
		{
			stack.push_back(str[i]);
		}
		for (int i = (int)N/2; i < N; ++i)
		{
			if (str[i] == stack.back())
			{
				stack.pop_back();
			}
			else
			{
				cout << "0";
				return 0;
			}
		}

		cout << "1";
	}
	else
	{
		for (int i = 0; i < (int)N/2; ++i)
		{
			stack.push_back(str[i]);
		}
		for (int i = (int)N/2+1; i < N; ++i)
		{
			if (str[i] == stack.back())
			{
				stack.pop_back();
			}
			else
			{
				cout << "0";
				return 0;
			}
		}

		cout << "1";
	}

	return 0;
}