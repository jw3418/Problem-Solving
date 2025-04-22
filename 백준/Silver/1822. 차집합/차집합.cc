#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <string>

using namespace std;

int main()
{
	int nA, nB; cin >> nA >> nB;

	set<int> A;
	for (int i = 0; i < nA; ++i)
	{
		int t; cin >> t;
		A.insert(t);
	}
	set<int> B;
	for (int i = 0; i < nB; ++i)
	{
		int t; cin >> t;
		B.insert(t);
	}

	set<int> result;
	int cnt = 0;
	for (auto &a : A)
	{
		if (B.find(a) != B.end())
		{
			continue;;
		}
		else
		{
			result.insert(a);
			cnt++;
		}
	}

	vector<int> ans(result.begin(), result.end());
	sort(ans.begin(), ans.end());
	cout << cnt << endl;
	for (auto it : ans)
	{
		cout << it << " ";
	}


    return 0;
}
