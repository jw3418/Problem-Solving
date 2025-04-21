#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
#include <set>

using namespace std;

int main()
{
	int N; cin >> N;
	vector<int> nums;
	for (int i = 0; i < N; ++i)
	{
		int t; cin >> t;
		nums.push_back(t);
	}

	int prev = nums[0];
	int l_cnt = 1; int max_l_cnt = 1;
	for (int i = 1; i < N; ++i)
	{
		if (nums[i] >= prev)
		{
			l_cnt++;
		}
		else
		{
			l_cnt = 1;
		}
		max_l_cnt = max(max_l_cnt, l_cnt);
		prev = nums[i];
	}

	prev = nums[0];
	int s_cnt = 1; int max_s_cnt = 1;
	for (int i = 1; i < N; ++i)
	{
		if (nums[i] <= prev)
		{
			s_cnt++;
		}
		else
		{
			max_s_cnt = max(max_s_cnt, s_cnt);
			s_cnt = 1;
		}
		max_s_cnt = max(max_s_cnt, s_cnt);
		prev = nums[i];
	}

	cout << max(max_l_cnt, max_s_cnt); 
	return 0;
}