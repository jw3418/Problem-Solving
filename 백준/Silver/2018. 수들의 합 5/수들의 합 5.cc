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

	int left = 1; int right = 1;
	int sum_ = left; int cnt = 0;
	while (left <= N)
	{
		if (sum_ == N)
		{
			cnt++;
		}
		if (sum_ >= N)
		{
			sum_ -= left;
			left++;
		}
		else
		{
			right++;
			sum_ += right;
		}
	}
	cout << cnt << endl;

    return 0;
}
