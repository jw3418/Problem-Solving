#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <map>
#include <string>

using namespace std;

int main()
{
	int N; cin >> N;
	unordered_set<string> visit;

	for (int i = 0; i < N; ++i)
	{
		string line; cin >> line;
		visit.insert(line);

		reverse(line.begin(), line.end());
		if (visit.find(line) != visit.end())
		{
			cout << line.length() << " " << line[(int)line.size()/2] << endl;
			return 0;
		}
	}

    return 0;
}
