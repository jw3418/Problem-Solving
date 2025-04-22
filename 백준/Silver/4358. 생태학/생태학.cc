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
		if (line.empty()) break;
		N++;
		Counter[line]++;
	}

	for (auto pair : Counter)
	{
		cout << pair.first << " " << fixed << setprecision(4) << (double)pair.second / N * 100 << endl;
	}

    return 0;
}
