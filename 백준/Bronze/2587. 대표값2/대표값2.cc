#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>

using namespace std;

int main()
{
	vector<int> number;
	for (int i = 0; i < 5; ++i)
	{
		int tmp; cin >> tmp;
		number.push_back(tmp);
	}

	sort(number.begin(), number.end());
	int sum_ = accumulate(number.begin(), number.end(), 0);

	cout << int(sum_) / 5 << endl;
	cout << number[2] << endl;
	
	return 0;
}