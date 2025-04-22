#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <map>
#include <tuple>
#include <string>
#include <iomanip>

using namespace std;

int main()
{
	int N = 0;
	string line;
	map<string, int> Counter;
	while (getline(cin, line))
	{
		N++;
		Counter[line]++;
	}

	cout << fixed << setprecision(4);

	for (auto pair : Counter)
	{
		cout << pair.first << " " << (double)pair.second / N * 100 << endl;
	}

    return 0;
}
