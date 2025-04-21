#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>


using namespace std;

int main()
{
	int N; cin >> N;

	if (N == 0)
	{
		cout << 0 << endl;
		return 0;
	}

	vector<int> grades(N);
	for (int i = 0; i < N; ++i)
	{
		cin >> grades[i];
	}

	sort(grades.begin(), grades.end());
	int cut = round(N * 0.15);
	
	int sum_ = 0;
	for (int i = cut; i < N-cut; ++i)
	{
		sum_ += grades[i];
	}
	cout << round((double)sum_ / (N - 2*cut));

	return 0;
}