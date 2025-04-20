#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <sstream>
#include <numeric>

using namespace std;

int main()
{
	vector<double> nums;
	double grade_sum = 0;
	for (int n = 0; n < 20; ++n)
	{
		string subject, grade, rank; cin >> subject >> grade >> rank;
		double grade_ = stod(grade);
		
		if (rank == "P") continue;
		grade_sum += grade_;

		if (rank == "A+") nums.push_back(grade_ * (4.5));
		else if (rank == "A0") nums.push_back(grade_ * (4.0));
		else if (rank == "B+") nums.push_back(grade_ * (3.5));
		else if (rank == "B0") nums.push_back(grade_ * (3.0));
		else if (rank == "C+") nums.push_back(grade_ * (2.5));
		else if (rank == "C0") nums.push_back(grade_ * (2.0));
		else if (rank == "D+") nums.push_back(grade_ * (1.5));
		else if (rank == "D0") nums.push_back(grade_ * (1.0));
		else if (rank == "F") nums.push_back(0);
	}
	cout << fixed;
    cout.precision(6);
	cout << accumulate(nums.begin(), nums.end(), 0.0) / grade_sum;

	return 0;
}