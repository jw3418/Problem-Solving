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

	vector<int> result;
	for (auto &a : A)
	{
		if (B.find(a) == B.end())
		{
			result.push_back(a);
		}
	}

	cout << result.size() << endl;
	for (auto it : result)
	{
		cout << it << " ";
	}


    return 0;
}
