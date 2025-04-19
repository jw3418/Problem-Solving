#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

int main()
{
	map<string, int> dictionary;
	dictionary["ABC"] = 3;
	dictionary["DEF"] = 4;
	dictionary["GHI"] = 5;
	dictionary["JKL"] = 6;
	dictionary["MNO"] = 7;
	dictionary["PQRS"] = 8;
	dictionary["TUV"] = 9;
	dictionary["WXYZ"] = 10;

	string str; cin >> str;
	int ans = 0;
	for (int i = 0; i < str.length(); ++i)
	{
		for (auto &dict : dictionary)
		{
			if (dict.first.find(str[i]) != string::npos)
			{
				ans += dict.second;
				break;
			}
		}
	}
	cout << ans;

	return 0;
}