#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <map>
#include <string>

using namespace std;

int main()
{
	int N; cin >> N; cin.ignore();
	vector<string> serial(N);
	for (int i = 0; i < N; ++i)
	{
		getline(cin, serial[i]);
	}

	sort(serial.begin(), serial.end(), [](const string &a, const string &b)
	{
		if (a.length() != b.length()) return a.length() < b.length();
		int a_sum = 0; int b_sum = 0;
		for (int i = 0; i < a.length(); ++i)
		{
			if ((a[i]-'0') >= 0 && (a[i]-'0') <= 9) a_sum += a[i]-'0';
		}
		for (int i = 0; i < b.length(); ++i)
		{
			if ((b[i]-'0') >= 0 && (b[i]-'0') <= 9) b_sum += b[i]-'0';
		}
		if (a_sum != b_sum) return a_sum < b_sum;
		return a < b;
	});

	for (auto str : serial)
	{
		cout << str << endl;
	}

    return 0;
}
