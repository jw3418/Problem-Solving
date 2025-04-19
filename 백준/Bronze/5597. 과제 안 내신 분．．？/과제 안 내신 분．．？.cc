#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

int main()
{
	set<int> set_;
	for (int i = 1; i <= 28; ++i)
	{
		int tmp; cin >> tmp;
		set_.insert(tmp);
	}

	for (int i = 1; i <= 30; ++i)
	{
		if (set_.find(i) != set_.end())
		{
			continue;
		}
		cout << i << endl;
	}

	return 0;
}