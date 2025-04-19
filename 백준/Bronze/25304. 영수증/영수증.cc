#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int X; cin >> X;
	int N; cin >> N;

	int Y = 0;
	for (int i = 0; i < N; ++i)
	{
		int a; int b;
		cin >> a >> b;
		Y += (a * b);
	}
	if (X == Y)
	{
		cout << "Yes";
	}
	else
	{
		cout << "No";
	}

	return 0;
}