#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
	int N; cin >> N;
	vector<vector<int>> birthday;
	map<vector<int>, string> dictionary;
	for (int n = 0; n < N; ++n)
	{
		string name; int day, month, year;
		cin >> name >> day >> month >> year;

		birthday.push_back({year, month, day});
		dictionary[{year, month, day}] = name;
	}

	sort(birthday.begin(), birthday.end(), [](const vector<int> &a, const vector<int> &b)
	{
		if (a[0] != b[0]) return a[0] < b[0];
		if (a[1] != b[1]) return a[1] < b[1];
		else return a[2] < b[2];
	});

	cout << dictionary[birthday[birthday.size()-1]] << endl;
	cout << dictionary[birthday[0]] << endl;

	return 0;
}