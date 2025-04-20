#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <sstream>

using namespace std;

int main()
{
	int R1, S; cin >> R1 >> S;

	int R2 = (int)2*S - R1;
	cout << R2;

	return 0;
}