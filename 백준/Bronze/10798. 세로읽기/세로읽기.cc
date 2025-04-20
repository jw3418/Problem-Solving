#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <sstream>

using namespace std;

int main()
{
	
	vector<vector<char>> board(5, vector<char>(15, '!'));

	for (int i = 0; i < 5; ++i)
	{
		string line;
		getline(cin, line);

		for (int j = 0; j < line.length(); ++j)
		{
			board[i][j] = line[j];
		}
	}

	string ans = "";
	for (int j = 0; j < 15; ++j)
	{
		for (int i = 0; i < 5; ++i)
		{
			if (board[i][j] != '!')
			{
				ans += board[i][j];
			}
		}
	}

	cout << ans;
	return 0;
}