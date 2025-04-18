#include <iostream>
#include <vector>

using namespace std;

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int main()
{
	int N; int B;
	cin >> N >> B;

	vector<char> iton =
	{'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
	'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
	'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
	'U', 'V', 'W', 'X', 'Y', 'Z'
	};

	vector<char> result;
	while (N >= B)
	{
		int X = (int)N / B;	//몫
		int Y = N % B;		//나머지

		result.push_back(iton[Y]);
		// cout << X << ", " << Y << endl;
		N = X;
	}
	result.push_back(iton[N]);

	for (int i = result.size()-1; i >= 0; --i)
	{
		cout << result[i];
	}

	return 0;
}