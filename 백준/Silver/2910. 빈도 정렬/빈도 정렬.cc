#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <tuple>
#include <string>

using namespace std;

int main()
{
	int N, C; cin >> N >> C;

	map<int, int> Counter;
	map<int, int> Order;
	for (int i = 0; i < N; ++i)
	{
		int t; cin >> t;
		Counter[t]++;
		if (Order.find(t) == Order.end())
		{
			Order[t] = N-i;
		}
	}

	vector<tuple<int, int, int>> container;	// {빈도, Order[실제값], 실제값}
	int idx = 0; int size_ = Counter.size();
	for (auto pair : Counter)
	{
		container.push_back({pair.second, Order[pair.first], pair.first});
		idx++;
	}

	sort(container.begin(), container.end(), [](const tuple<int, int, int> &a, const tuple<int, int, int> &b)
	{
		return a > b;
	});

	for (int i = 0; i < container.size(); ++i)
	{
		auto [cnt, b, val] = container[i];
		for (int j = 0; j < cnt; ++j)
		{
			cout << val << " ";
		}
	}

    return 0;
}
