#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>

using namespace std;

int main()
{
	int N; cin >> N;

	map<string, bool> dict;
	for (int i = 0; i < N; ++i)
	{
		string A, B; cin >> A >> B;
		if (dict.find(A) == dict.end())
		{
			dict[A] = false;
		}
		if (dict.find(B) == dict.end())
		{
			dict[B] = false;
		}

		if (dict[A] || dict[B] || A == "ChongChong" || B == "ChongChong")
		{
			dict[A] = true;
			dict[B] = true;
		}
	}

	int ans = 0;
	for (auto pair : dict)
	{
		if (pair.second)
		{
			ans++;
		}
	}
	cout << ans;

    return 0;
}
