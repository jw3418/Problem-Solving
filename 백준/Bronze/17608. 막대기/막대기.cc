#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int N; cin >> N;
	vector<int> Height(N);
	for (int i = 0; i < N; ++i)
	{
		cin >> Height[i];
	}

	vector<int> stack;
	for (int i = N-1; i >= 0; --i)
	{
		if (!stack.empty() && stack.back() >= Height[i])
		{
			continue;
		}
		else
		{
			stack.push_back(Height[i]);
		}
	}
	cout << stack.size() << endl;

    return 0;
}
