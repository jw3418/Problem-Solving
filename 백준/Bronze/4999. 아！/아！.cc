#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <map>
#include <string>

using namespace std;

int main()
{
	string line1; getline(cin, line1);
	string line2; getline(cin, line2);
	if (line1.length() < line2.length())
	{
		cout << "no" << endl;
	}
	else
	{
		cout << "go" << endl;
	}

    return 0;
}
