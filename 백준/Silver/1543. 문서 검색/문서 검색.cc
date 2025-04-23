#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <map>
#include <string>

using namespace std;

int main()
{
	string target; getline(cin, target);
	string line; getline(cin, line);
	int len = line.length();
	if (len > target.length())
	{
		cout << 0 << endl;
		return 0;
	}

	int cnt = 0;
	for (int i = 0; i < target.length() - len + 1; ++i)
	{
		if (target.substr(i, len) == line)
		{
			cnt++;
			i += len-1;
		}
	}
	cout << cnt << endl;

    return 0;
}
