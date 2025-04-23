#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <map>
#include <string>

using namespace std;

int main()
{
	string A, B; cin >> A >> B; cin.ignore();

	int min_diff_cnt = 1e9;
	int idx = -1;
	for (int i = 0; i < B.length() - A.length() + 1; ++i)
	{
		string target = B.substr(i, A.length());
		int cnt = 0;
		for (int j = 0; j < target.length(); ++j)
		{
			if (target[j] != A[j])
			{
				cnt++;
			}
		}
		if (min_diff_cnt > cnt)
		{
			min_diff_cnt = cnt;
		}
	}
	cout << min_diff_cnt << endl;

    return 0;
}
