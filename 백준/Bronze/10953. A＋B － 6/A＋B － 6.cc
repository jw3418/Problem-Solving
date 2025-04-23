#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <map>
#include <string>

using namespace std;

int main()
{
	int N; cin >> N; cin.ignore();
	string line;
	for (int n = 0; n < N; ++n)
	{
		getline(cin, line);
		int A, B;
		A = line[0] - '0'; B = line[2] - '0';
		cout << A+B << endl;
	}

    return 0;
}
