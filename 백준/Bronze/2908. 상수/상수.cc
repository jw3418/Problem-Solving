#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int A; int B;
	cin >> A >> B;

	string A_str = to_string(A); string B_str = to_string(B);
	int N = A_str.length();

	string rA_str = ""; string rB_str = "";
	for (int i = N-1; i >= 0; --i)
	{
		rA_str += A_str[i];
		rB_str += B_str[i];
	}

	A = stoi(rA_str); B = stoi(rB_str);

	if (A > B)
	{
		cout << A;
	}
	else
	{
		cout << B;
	}

	return 0;
}